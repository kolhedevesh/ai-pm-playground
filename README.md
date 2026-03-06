# AI PM Playground 🚀

AI PM Playground is a Streamlit-based web application that acts as an **AI Product Manager copilot**.  
It helps generate **Product Requirements Documents (PRDs), product ideas, and product strategy insights** using a large language model.

The project demonstrates how AI can assist product managers in **ideation, documentation, and decision-making workflows**.

---

## 🌐 Live App

Try the deployed app here:

https://ai-pm-playground.streamlit.app

---

## 🧠 What This App Does

The AI PM Playground allows users to interact with an AI model to:

- Generate **Product Requirement Documents (PRDs)**
- Brainstorm **product ideas and feature concepts**
- Explore **product strategy and roadmap thinking**
- Get guidance on **metrics, product design, and product decisions**

Example prompts:

```
Create a PRD for an AI customer support agent
Generate feature ideas for a fintech budgeting app
What metrics should I track for an AI chatbot product?
Design a roadmap for an AI writing assistant
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
Frontend | Streamlit |
LLM API | Groq API |
Model | Llama-3.3-70B-Versatile |
Language | Python |
Deployment | Streamlit Community Cloud |
Version Control | GitHub |

---

## 🏗 Architecture

User Input  
↓  
Streamlit UI  
↓  
Groq API  
↓  
LLM Model  
↓  
Generated Product Insights / PRDs  

---

## 📂 Project Structure

```
ai-pm-playground
│
├── app.py
├── requirements.txt
├── test_ollama.py
├── .streamlit/
│   └── secrets.toml
└── .gitignore
```

---

## 🔑 Environment Setup

The application requires a **Groq API key**.

Create a file:

```
.streamlit/secrets.toml
```

Add:

```
GROQ_API_KEY="your_api_key_here"
```

For Streamlit Cloud deployment, add this key under:

```
App Settings → Secrets
```

---

## 🖥 Run Locally

Clone the repository:

```
git clone https://github.com/kolhedevesh/ai-pm-playground.git
cd ai-pm-playground
```

Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

---

## 🚀 Deployment

This project is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the repository to GitHub  
2. Connect the repository to Streamlit Cloud  
3. Select  
   - Repository: `kolhedevesh/ai-pm-playground`  
   - Branch: `main`  
   - Main file: `app.py`  
4. Add `GROQ_API_KEY` under Secrets  
5. Deploy

---

## 🎯 Why This Project

This project explores how **LLMs can augment product management workflows**, including:

- PRD drafting
- product ideation
- roadmap thinking
- product analytics guidance

It demonstrates how AI can act as a **co-pilot for product managers**, accelerating early-stage product development.

---

## 🔮 Possible Future Improvements

- PRD templates with structured sections
- Feature prioritization using **RICE scoring**
- AI-generated **product roadmaps**
- User story generation
- Export PRDs to **Notion / Markdown / PDF**
- Multi-agent product ideation workflows

---

## 👤 Author

Devesh Kolhe  

GitHub  
https://github.com/kolhedevesh

---

## 📜 License

MIT License
