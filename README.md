# LinkedIn AI Chatbot

**An AI-powered assistant that brings your LinkedIn profile to life.**  
Upload your LinkedIn PDF and chat with a conversational AI that answers questions about your experience, skills, and career — powered by **OpenAI API**, **PyPDF**, and **Gradio**.

---

## 🚀 Key Features
- **Interactive Agent** – Engages with your LinkedIn profile and responds to questions about your background, skills, and experience.  
- **PDF Parsing** – Uses **PyPDF** to extract and process text from your LinkedIn PDF (or optional summary).  
- **Conversational UI** – Built with **Gradio**, providing a clean, chat-based interface.  
- **Context-Aware Responses** – Powered by the **OpenAI API** for intelligent, relevant answers.  

---

## 🛠️ Tech Stack
- Python  
- OpenAI API  
- PyPDF  
- Gradio  
- python-dotenv (for environment variable management)  

---

## 📂 Project Structure
```
LinkedIn-AI-Chatbot/
├─ app.py                  # Gradio app
├─ requirements.txt        # Dependencies
├─ README.md               # Project overview (this file)
├─ LICENSE                 # MIT License
├─ .gitignore              # Git ignored files
├─ me/                     # My LinkedIn data Aug 2025 (now included in repo)
│  ├─ linkedin.pdf         # Exported LinkedIn profile
│  └─ summary.txt          # Optional profile summary
└─ notebook.ipynb          # main code 
```

---

## ⚡ Setup & Run

1. **Clone this repository**
```bash
git clone https://github.com/joonasisoininen/LinkedIn-AI-Chatbot.git
cd LinkedIn-AI-Chatbot
```

2. **Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables in `.env`**
```bash
OPENAI_API_KEY=sk-...
MODEL=gpt-4o-mini
```

5. **Run the app**
```bash
python3 app.py
```
Then open the local Gradio URL shown in your terminal.

---

## 💡 Skills Showcased
- OpenAI API • PyPDF • Gradio • Python  
- NLP • Conversational AI • API Integration  
- Chatbot Development • Data Extraction & Transformation  

---

## 🎯 Why This Project Matters
This chatbot is more than just code — it’s a **modern approach to personal branding**. It demonstrates:
- Proficiency in AI integration and Python libraries  
- Creativity in applying AI to career storytelling  
- UX thinking by making professional info interactive  

---

*Note: The `me/` directory now contains `linkedin.pdf` and `summary.txt` for demonstration purposes.*
