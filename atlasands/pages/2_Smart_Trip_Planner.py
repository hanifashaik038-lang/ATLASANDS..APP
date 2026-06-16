# pages/2_Smart_Trip_Planner.py
import streamlit as st
from utils.image_utils import load_css
from utils.ai import ask_ai
from utils.budget import estimate_budget
from data.constants import TRAVEL_STYLES, ADVENTURE_LEVELS, TRANSPORT

st.set_page_config(page_title="Smart Trip Planner · ATLASANDS", page_icon="🧭", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>Smart Trip Planner</h2>"
    "<div class='sub'>Tell us about you — we'll craft the perfect Indian adventure</div></div>",
    unsafe_allow_html=True,
)

with st.form("planner"):
    c1, c2 = st.columns(2)
    start = c1.text_input("Starting City", "Mumbai")
    dest = c2.text_input("Destination", "Goa")

    c3, c4, c5 = st.columns(3)
    budget = c3.number_input("Budget (INR)", 5000, 300000, 25000, 1000)
    days = c4.slider("Days", 1, 21, 5)
    style = c5.selectbox("Style", TRAVEL_STYLES)

    interests = st.text_input("Interests", "beach, food, nightlife")

    c6, c7 = st.columns(2)
    transport = c6.selectbox("Preferred Transport", TRANSPORT)
    level = c7.selectbox("Adventure Level", ADVENTURE_LEVELS)

    submitted = st.form_submit_button("✨ Generate My Itinerary")

# Live estimate card
est = estimate_budget(days, style, level)
st.markdown(
    f"<div class='glass-card' style='text-align:center'>"
    f"<h3>Live Budget Estimate</h3>"
    f"<p style='font-size:1.4rem'><b>INR {est:,}</b> for {days} days · {style}</p></div>",
    unsafe_allow_html=True,
)

if submitted:
    with st.spinner("Designing your perfect trip..."):
        prompt = (
            f"Plan a {days}-day {style} trip from {start} to {dest}. "
            f"Budget INR {budget}. Interests: {interests}. "
            f"Transport: {transport}. Adventure: {level}. "
            "Give a day-by-day itinerary with timings, suggested food, stay options, and approximate costs. "
            "Use bullet points and clear headings."
        )
        result = ask_ai(prompt)
    st.markdown(f"<div class='glass-card'>{result}</div>", unsafe_allow_html=True)

    # Save to session for the Saved Trips page
    st.session_state.setdefault("saved_trips", []).append({
        "dest": dest, "days": days, "style": style, "budget": budget, "plan": result
    })
    st.success("Trip saved! Visit the **Saved Trips** page to revisit it later.")
