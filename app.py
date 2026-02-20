import streamlit as st
from google import genai
from google.genai import types
import logging

# --- Config ---
PROJECT_ID = "spartacus-dental-2026"
REGION = "us-central1"

# Pick a model:
# The codelab mentions gemini-2.5-flash, but you confirmed gemini-2.0-flash-001 works in your project.
GEMINI_MODEL_NAME = "gemini-2.0-flash-001"

temperature = 0.2
top_p = 0.95

system_instructions = """
You are Spartacus, a dental insurance AI assistant.
You help users understand dental coverage, benefits, deductibles, waiting periods, and pre-authorizations.
Be concise, explain like a helpful clinic assistant, and add a short “next step” suggestion.
Never request full SSNs or full insurance member IDs.
"""

# --- Initialize Vertex AI (GenAI client) ---
try:
    client = genai.Client(
        vertexai=True,
        project=PROJECT_ID,
        location=REGION,
    )
    logging.info(f"VertexAI Client initialized with model {GEMINI_MODEL_NAME}")
except Exception as e:
    st.error(f"Error initializing VertexAI client: {e}")
    st.stop()

def call_model(prompt: str, model_name: str) -> str:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
                top_p=top_p,
                system_instruction=system_instructions,
            ),
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# --- Streamlit UI ---
st.title("Spartacus: Dental Insurance Chatbot 🦷")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I’m Spartacus. What dental insurance question can I help with today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Spartacus is thinking..."):
        model_response = call_model(prompt, GEMINI_MODEL_NAME)

    st.session_state.messages.append({"role": "assistant", "content": model_response})
    st.chat_message("assistant").write(model_response)