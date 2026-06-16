# utils/ai.py
# Thin wrapper around the OpenAI Python SDK.
import streamlit as st
from data.prompts import SYSTEM_PROMPT

try:
    from openai import OpenAI
except Exception:
    OpenAI = None


def _get_client():
    """Return an OpenAI client if a key exists, else None."""
    if OpenAI is None:
        return None
    api_key = st.secrets.get("OPENAI_API_KEY", "") if hasattr(st, "secrets") else ""
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def ask_ai(user_message: str, history=None, model: str = "gpt-4o-mini") -> str:
    """Send a message to OpenAI and return a string reply."""
    client = _get_client()
    if client is None:
        return ("AI not configured yet. Add OPENAI_API_KEY in `.streamlit/secrets.toml` "
                "(or in Streamlit Cloud > App settings > Secrets) to unlock AI features.")
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        msgs.extend(history)
    msgs.append({"role": "user", "content": user_message})
    try:
        resp = client.chat.completions.create(
            model=model, messages=msgs, temperature=0.7, max_tokens=900
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"AI error: {e}"
