import streamlit as st
from utils.image_utils import load_css
from utils.ai import ask_ai

st.set_page_config(page_title="Travel Journal · ATLASANDS", page_icon="📖", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>AI Travel Journal</h2>"
    "<div class='sub'>Turn your memories into a beautiful story</div></div>",
    unsafe_allow_html=True,
)

dest = st.text_input("Where did you go?", "Udaipur")
days = st.slider("Trip Length (days)", 1, 21, 4)
highlights = st.text_area(
    "Few highlights / memories",
    "Lake Pichola boat ride, palace tour, rooftop dinner under stars, royal Rajasthani thali",
)
mood = st.selectbox("Tone of the journal", ["Poetic & dreamy", "Lively & fun", "Reflective & calm", "Adventurous"])

if st.button("📖 Write My Journal"):
    with st.spinner("Penning your story..."):
        out = ask_ai(
            f"Write a {mood.lower()} day-by-day travel journal for a {days}-day trip to {dest}, India. "
            f"Highlights to include: {highlights}. Make it elegant, descriptive, around 350-500 words, "
            "with day-wise headings. End with one beautiful closing line."
        )
    st.markdown(f"<div class='glass-card'>{out}</div>", unsafe_allow_html=True)

    st.download_button(
        "💾 Download as Text",
        data=out,
        file_name=f"{dest}_journal.txt",
        mime="text/plain",
    )
