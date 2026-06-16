# pages/4_Packing_Assistant.py
import streamlit as st
from utils.image_utils import load_css
from utils.packing import default_packing
from utils.ai import ask_ai
from data.constants import SEASONS

st.set_page_config(page_title="Packing Assistant · ATLASANDS", page_icon="🎒", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>Packing Assistant</h2>"
    "<div class='sub'>Never forget the essentials again</div></div>",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
dest = c1.text_input("Destination", "Manali")
season = c2.selectbox("Season", SEASONS)
activities = c3.text_input("Planned Activities", "trekking, sightseeing, food walks")

if st.button("🎒 Generate My Packing List"):
    base = default_packing(season, activities)
    with st.spinner("Asking AI for smart picks..."):
        ai_list = ask_ai(
            f"Give 10 niche packing items (not common things like soap or phone) for a {season} trip "
            f"to {dest}, India, doing: {activities}. Return as a clean bullet list with a short reason for each."
        )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<div class='glass-card'><h3>Essentials</h3>" +
            "".join([f"<p>✓ {x}</p>" for x in base]) + "</div>",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(f"<div class='glass-card'><h3>AI Smart Picks</h3>{ai_list}</div>",
                    unsafe_allow_html=True)
