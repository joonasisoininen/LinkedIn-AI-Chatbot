import os
from dotenv import load_dotenv
from pypdf import PdfReader
import gradio as gr

# OpenAI (>=1.0 client)
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")

client = OpenAI(api_key=OPENAI_API_KEY)

def load_profile(pdf_path: str, summary_path: str | None = None) -> str:
    """Extract text from LinkedIn PDF and (optionally) append summary.txt."""
    content = []
    if os.path.exists(pdf_path):
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            try:
                content.append(page.extract_text() or "")
            except Exception:
                pass
    if summary_path and os.path.exists(summary_path):
        with open(summary_path, "r", encoding="utf-8") as f:
            content.append("\nSUMMARY:\n" + f.read())
    return "\n".join(content).strip()

PROFILE_TEXT = load_profile("data/linkedin.pdf", "data/summary.txt")

SYSTEM_PROMPT = (
    "You are a helpful professional assistant that represents the user's career. "
    "Answer questions accurately and concisely, using only the information in the provided profile text. "
    "If something is unknown, say you don't have that information."
)

def chat(message, history):
    context = PROFILE_TEXT if PROFILE_TEXT else "Profile content not found."
    user_prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"--- PROFILE TEXT START ---\n{context}\n--- PROFILE TEXT END ---\n\n"
        f"User question: {message}"
    )
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system", "content": SYSTEM_PROMPT},
                {"role":"user", "content": user_prompt}
            ],
            temperature=0.3,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks(title="AI Career Agent") as demo:
    gr.Markdown("# AI Career Agent\nAsk about the profile to learn more.")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="Ask about experience, skills, projects...")
    clear = gr.Button("Clear")

    def respond(user_message, chat_history):
        bot_message = chat(user_message, chat_history)
        chat_history = chat_history + [(user_message, bot_message)]
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()