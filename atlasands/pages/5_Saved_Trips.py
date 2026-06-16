import streamlit as st
from utils.image_utils import load_css

st.set_page_config(page_title="Saved Trips · ATLASANDS", page_icon="📌", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>Saved Trips</h2>"
    "<div class='sub'>Your travel ideas, ready to revisit anytime</div></div>",
    unsafe_allow_html=True,
)

trips = st.session_state.get("saved_trips", [])

if not trips:
    st.info("You haven't saved any trips yet. Visit **Smart Trip Planner** to create one.")
else:
    for i, t in enumerate(trips):
        st.markdown(
            f"<div class='glass-card'>"
            f"<h3>✈️ {t['dest']} — {t['days']} days · {t.get('style','')}</h3>"
            f"<p><b>Budget:</b> INR {t.get('budget',0):,}</p>"
            f"<hr>{t['plan']}</div>",
            unsafe_allow_html=True,
        )
        if st.button(f"🗑️ Remove trip {i+1}", key=f"rm_{i}"):
            st.session_state.saved_trips.pop(i)
            st.rerun()
