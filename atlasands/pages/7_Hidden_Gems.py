# pages/7_Hidden_Gems.py
import streamlit as st
from utils.image_utils import load_css
from utils.ai import ask_ai

st.set_page_config(page_title="Hidden Gems · ATLASANDS", page_icon="💎", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>Hidden Gems of India</h2>"
    "<div class='sub'>Places only locals know about</div></div>",
    unsafe_allow_html=True,
)

state = st.text_input("Which state or region?", "Himachal Pradesh")
vibe = st.selectbox("Vibe you want", ["Peaceful", "Scenic", "Cultural", "Adventurous", "Spiritual"])

if st.button("💎 Reveal Hidden Gems"):
    with st.spinner("Asking the locals (via AI)..."):
        out = ask_ai(
            f"List 6 lesser-known {vibe.lower()} hidden gems in {state}, India. "
            "For each: name, why special, best time to visit, approximate budget per day in INR, "
            "and one local food to try. Use a beautiful structured bullet format."
        )
    st.markdown(f"<div class='glass-card'>{out}</div>", unsafe_allow_html=True)
