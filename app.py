import streamlit as st
import random
from groq import Groq

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI PM Playground",
    layout="centered"
)

# -------------------------------
# Groq API Client Setup
# -------------------------------
if "GROQ_API_KEY" not in st.secrets:
    st.error("Groq API key not found. Please add GROQ_API_KEY to Streamlit secrets.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -------------------------------
# Model Configuration
# -------------------------------
MODEL_NAME = "llama-3.3-70b-versatile"

# -------------------------------
# Title
# -------------------------------
st.title("AI PM Playground")
st.caption("Your Senior AI PM Copilot")

# -------------------------------
# System Persona
# -------------------------------
SYSTEM_PROMPT = """
You are a Senior AI Product Manager mentoring an aspiring AI PM.

You:
- Think in product frameworks
- Are practical and structured
- Explain trade-offs
- Avoid buzzwords
- Give real-world examples

Your goal is to improve the user's product thinking.
"""

# -------------------------------
# Example Placeholders
# -------------------------------
EXAMPLES = [
    "Create a PRD for an AI customer support agent",
    "Design an MVP for an AI recruiting assistant",
    "What metrics should I track for an AI chatbot?",
    "Evaluate this product idea from a PM lens",
    "Suggest AI features for a consumer fintech app"
]

# -------------------------------
# Session State Init
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "placeholder" not in st.session_state:
    st.session_state.placeholder = random.choice(EXAMPLES)

# -------------------------------
# Render Chat History
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Placeholder Logic (Stable)
# -------------------------------
placeholder_text = st.session_state.placeholder


# -------------------------------
# Input Box
# -------------------------------
user_input = st.chat_input(
    placeholder=placeholder_text
)

# -------------------------------
# On User Message
# -------------------------------
if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    convo = [{"role": "system", "content": SYSTEM_PROMPT}]
    convo.extend(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Thinking like a PM..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=convo
                )

                answer = response.choices[0].message.content
                st.markdown(answer)

            except Exception as e:
                st.error(f"Model request failed: {str(e)}")
                st.stop()

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
