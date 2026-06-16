# app.py — ATLASANDS Premium Homepage
import streamlit as st
from utils.image_utils import load_css, hero_html, dest_card_html
from utils.budget import estimate_budget
from data.destinations import DESTINATIONS, CATEGORIES, HERO_IMAGES
from data.constants import (
    APP_NAME, TAGLINE, SUBTAGLINE,
    TRAVEL_STYLES, ADVENTURE_LEVELS, WEATHER_PREF,
)

# ---------- Page config ----------
st.set_page_config(
    page_title=f"{APP_NAME} | Premium India Travel",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_css()

# ---------- Sidebar (filters & trip summary) ----------
with st.sidebar:
    st.markdown(f"## ✨ {APP_NAME}")
    st.markdown("<p style='font-style:italic'>Your premium India travel companion</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### Filters")
    category = st.selectbox("Category", CATEGORIES, key="f_category")
    budget = st.slider("Budget (INR)", 5000, 60000, 25000, 1000, key="f_budget")
    days = st.slider("Travel Days", 1, 21, 5, key="f_days")
    style = st.selectbox("Travel Style", TRAVEL_STYLES, key="f_style")
    level = st.selectbox("Adventure Level", ADVENTURE_LEVELS, key="f_level")
    weather = st.selectbox("Weather Preference", WEATHER_PREF, key="f_weather")

    st.markdown("---")
    st.markdown("### Quick Trip Summary")
    est = estimate_budget(days, style, level)
    st.info(f"**{style}** · {days} days · {category}\n\nEstimated cost: **INR {est:,}**")

    st.markdown("---")
    st.markdown("### Navigation")
    st.markdown("""
    - 🤖 AI Assistant
    - 🧭 Smart Trip Planner
    - 💰 Expense Tracker
    - 🎒 Packing Assistant
    - 📌 Saved Trips
    - 💵 Budget Optimizer
    - 💎 Hidden Gems
    - 📖 Travel Journal
    """)

# ---------- Hero ----------
st.markdown(hero_html(HERO_IMAGES[0], APP_NAME, TAGLINE), unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align:center;font-size:1.25rem;font-style:italic;color:#5B3A1E;'>{SUBTAGLINE}</p>",
    unsafe_allow_html=True,
)

# ---------- CTA buttons ----------
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("✨  Start Planning  ✨", use_container_width=True):
        st.switch_page("pages/2_Smart_Trip_Planner.py")

# ---------- Welcome ----------
st.markdown(
    "<div class='section-title'><h2>Welcome, Wanderer</h2>"
    "<div class='sub'>Where will your story unfold today?</div></div>",
    unsafe_allow_html=True,
)

w1, w2, w3 = st.columns(3)
w1.markdown(
    "<div class='glass-card'><h3>AI Concierge</h3>"
    "<p>Your personal travel assistant trained on India's most beautiful destinations. "
    "Ask anything — itineraries, food, hidden spots.</p></div>",
    unsafe_allow_html=True,
)
w2.markdown(
    "<div class='glass-card'><h3>Smart Budget</h3>"
    "<p>Plan trips that fit your wallet without compromising the experience. "
    "Live estimates and AI optimisation.</p></div>",
    unsafe_allow_html=True,
)
w3.markdown(
    "<div class='glass-card'><h3>Hidden Gems</h3>"
    "<p>Discover off-beat places loved by locals and missed by ordinary tourists. "
    "AI-powered discovery.</p></div>",
    unsafe_allow_html=True,
)

# ---------- Why choose us ----------
st.markdown("<div class='section-title'><h2>Why Choose ATLASANDS</h2></div>", unsafe_allow_html=True)
why = [
    ("🌿", "Curated", "Hand-picked destinations across India"),
    ("⚡", "AI-Powered", "Itineraries generated in seconds"),
    ("💎", "Premium", "Luxury feel without the price tag"),
    ("🛡️", "Safe", "Verified info & travel safety tips"),
]
cols = st.columns(4)
for col, (i, t, d) in zip(cols, why):
    col.markdown(
        f"<div class='glass-card' style='text-align:center;min-height:200px;'>"
        f"<div style='font-size:3rem;line-height:1'>{i}</div>"
        f"<h3 style='margin:8px 0'>{t}</h3>"
        f"<p>{d}</p></div>",
        unsafe_allow_html=True,
    )

# ---------- Featured destinations ----------
st.markdown(
    "<div class='section-title'><h2>Featured Destinations</h2>"
    "<div class='sub'>The most beloved escapes in India</div></div>",
    unsafe_allow_html=True,
)

# Apply filters
filtered = [
    d for d in DESTINATIONS
    if (category == "All" or d["category"] == category)
    and d["budget"] <= budget
]

if not filtered:
    st.warning("No destinations match your filters. Try increasing the budget.")
else:
    rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
    for row in rows:
        cols = st.columns(3)
        for col, dest in zip(cols, row):
            with col:
                st.markdown(dest_card_html(dest), unsafe_allow_html=True)

# ---------- Popular Categories ----------
st.markdown("<div class='section-title'><h2>Popular Categories</h2></div>", unsafe_allow_html=True)
pop = [
    ("🏖️", "Beach", "Goa · Andaman · Varkala"),
    ("⛰️", "Hill Station", "Manali · Coorg · Kashmir"),
    ("🏛️", "Heritage", "Jaipur · Udaipur · Hampi"),
    ("🐅", "Wildlife", "Jim Corbett · Ranthambore · Kaziranga"),
    ("🪂", "Adventure", "Ladakh · Rishikesh · Spiti"),
    ("🕉️", "Spiritual", "Varanasi · Haridwar · Tirupati"),
]
for i in range(0, len(pop), 3):
    cols = st.columns(3)
    for col, (ic, t, d) in zip(cols, pop[i:i+3]):
        col.markdown(
            f"<div class='glass-card' style='text-align:center;'>"
            f"<div style='font-size:2.6rem'>{ic}</div>"
            f"<h3>{t}</h3><p>{d}</p></div>",
            unsafe_allow_html=True,
        )

# ---------- AI Features ----------
st.markdown(
    "<div class='section-title'><h2>AI-Powered Magic</h2>"
    "<div class='sub'>Twelve intelligent features at your fingertips</div></div>",
    unsafe_allow_html=True,
)
ai_features = [
    ("🧭", "Itinerary Generator", "Personalised day-by-day plans"),
    ("💵", "Budget Optimizer", "Maximise experience per rupee"),
    ("💬", "Travel Assistant", "24/7 AI concierge chat"),
    ("💎", "Hidden Gems", "Find untouched local treasures"),
    ("🎒", "Packing Lists", "Smart climate-aware suggestions"),
    ("📊", "Expense Analyzer", "Track every rupee spent"),
    ("🛣️", "Route Planner", "Optimal routes (AI-estimated)"),
    ("🍛", "Restaurant Finder", "Best local food picks"),
    ("🌅", "Scenic Spots", "Most beautiful viewpoints"),
    ("📖", "Travel Journal", "AI writes your memories"),
    ("☀️", "Weather Tips", "Season-based recommendations"),
    ("🌱", "Eco Score", "Travel sustainably"),
]
for i in range(0, len(ai_features), 4):
    cols = st.columns(4)
    for col, (ic, t, d) in zip(cols, ai_features[i:i+4]):
        col.markdown(
            f"<div class='glass-card' style='text-align:center;min-height:200px;'>"
            f"<div style='font-size:2.4rem'>{ic}</div>"
            f"<h3 style='margin:8px 0'>{t}</h3><p>{d}</p></div>",
            unsafe_allow_html=True,
        )

# ---------- Testimonials ----------
st.markdown("<div class='section-title'><h2>What Travellers Say</h2></div>", unsafe_allow_html=True)
testimonials = [
    ("Priya, Mumbai", "ATLASANDS planned my Ladakh trip in 30 seconds. Magical!"),
    ("Arjun, Bengaluru", "The AI found hidden cafés in Coorg I'd never have seen otherwise."),
    ("Sneha, Delhi", "Budget breakdown was so accurate. Saved INR 8,000 on my Goa trip."),
]
cols = st.columns(3)
for col, (n, q) in zip(cols, testimonials):
    col.markdown(
        f"<div class='glass-card'>"
        f"<p style='font-size:1.1rem;font-style:italic'>“{q}”</p>"
        f"<p style='text-align:right;font-weight:700'>— {n}</p></div>",
        unsafe_allow_html=True,
    )

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;padding:30px;'>"
    "<h2 style='font-family:Great Vibes,cursive;margin:0'>ATLASANDS</h2>"
    "<p style='font-style:italic;color:#5B3A1E'>Crafted with love for Indian travellers · © 2026</p>"
    "</div>",
    unsafe_allow_html=True,
)

# ---------- Floating AI button ----------
st.markdown(
    "<a class='fab' href='/AI_Assistant' title='Ask the AI Concierge'>🤖</a>",
    unsafe_allow_html=True,
)
