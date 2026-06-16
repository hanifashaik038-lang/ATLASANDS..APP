# pages/1_AI_Assistant.py
# Premium AI travel concierge chat.
import streamlit as st
from utils.image_utils import load_css
from utils.ai import ask_ai

st.set_page_config(page_title="AI Assistant · ATLASANDS", page_icon="🤖", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>AI Travel Concierge</h2>"
    "<div class='sub'>Ask anything about travel in India — itineraries, food, hidden spots, budgets.</div></div>",
    unsafe_allow_html=True,
)

# Chat history is stored in session state so it persists across reruns.
if "chat" not in st.session_state:
    st.session_state.chat = []

# Suggested quick prompts
st.markdown("<div class='glass-card'><h3>Try asking</h3>"
            "<p>• Plan a 5-day budget trip to Kerala<br>"
            "• Hidden gems near Manali<br>"
            "• Vegetarian food guide for Varanasi<br>"
            "• Best time to visit Andaman</p></div>",
            unsafe_allow_html=True)

# Render previous messages
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Chat input box
if prompt := st.chat_input("Where would you like to go?"):
    st.session_state.chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Crafting your reply..."):
            reply = ask_ai(prompt, st.session_state.chat[:-1])
        st.markdown(reply)
    st.session_state.chat.append({"role": "assistant", "content": reply})

# Clear button
if st.session_state.chat:
    if st.button("Clear conversation"):
        st.session_state.chat = []
        st.rerun()
