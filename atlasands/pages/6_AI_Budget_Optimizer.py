# pages/6_AI_Budget_Optimizer.py
import streamlit as st
from utils.image_utils import load_css
from utils.ai import ask_ai

st.set_page_config(page_title="Budget Optimizer · ATLASANDS", page_icon="💵", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>AI Budget Optimizer</h2>"
    "<div class='sub'>Make every rupee count</div></div>",
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
dest = c1.text_input("Destination", "Kerala")
budget = c2.number_input("Budget (INR)", 5000, 300000, 30000, 1000)
days = st.slider("Trip Length (days)", 1, 21, 6)

if st.button("💡 Optimize My Budget"):
    with st.spinner("Crunching numbers..."):
        out = ask_ai(
            f"Optimize a INR {budget} budget for {days} days in {dest}, India. "
            "Give detailed breakdown: stay, food, transport, activities, buffer. "
            "Suggest 5 specific money-saving tips. Use INR throughout, bullet points and bold headings."
        )
    st.markdown(f"<div class='glass-card'>{out}</div>", unsafe_allow_html=True)
