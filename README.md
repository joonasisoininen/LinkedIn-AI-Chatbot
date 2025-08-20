# AI Career Agent

An **AI-powered professional assistant** that brings a LinkedIn profile to life, combining **OpenAI API**, **PyPDF**, and **Gradio** into a seamless experience.

- Transforms a LinkedIn profile (PDF) into an **interactive agent** that answers questions about background, skills, and experience
- Parses and structures professional data from PDF using **PyPDF**
- Delivers engaging, human‑like responses via a **Gradio** conversational UI powered by **OpenAI API**
- Demonstrates how AI can enhance **career storytelling, networking, and professional representation**

## Tech Stack

- **Python**
- **OpenAI API**
- **PyPDF**
- **Gradio**
- `python-dotenv` for env management

## Project Structure

```
ai-career-agent/
├─ app.py                 # Gradio app
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ .gitignore
├─ data/                  # Place linkedin.pdf and optional summary.txt here (not tracked)
│  └─ .gitkeep
└─ notebooks/
   └─ 3_lab3.ipynb        # Original lab notebook (reference)
```

## Setup

1) **Clone** and create a virtual environment
```bash
git clone https://github.com/<your-username>/ai-career-agent.git
cd ai-career-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2) **Set environment variables**
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=sk-...
MODEL=gpt-4o-mini
```

3) **Add your LinkedIn data**
- Export your LinkedIn profile to PDF and save it as `data/linkedin.pdf`
- (Optional) Create `data/summary.txt` with key highlights

4) **Run the app**
```bash
python app.py
```
Then open the printed local URL in your browser.

## Skills (good to list on LinkedIn)

- **OpenAI API**, **PyPDF**, **Gradio**, **Python**
- **NLP**, **Conversational AI**, **API Integration**
- **Chatbot Development**, **Data Extraction & Transformation**

---

**Attribution**: Includes an adapted version of a lab notebook in `notebooks/3_lab3.ipynb` for reference.