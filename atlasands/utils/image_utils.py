# utils/image_utils.py
# Helpers for loading CSS and rendering crisp images via HTML.
import os
import streamlit as st


def load_css(path: str = None):
    """Inject the global stylesheet into the current page."""
    if path is None:
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(here, "styles", "style.css")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def hero_html(image_url: str, title: str, subtitle: str) -> str:
    """Return HTML for the full-width hero banner."""
    return f"""
    <div class="hero">
        <img src="{image_url}" alt="hero image">
        <div class="hero-text">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    </div>
    """


def dest_card_html(dest: dict) -> str:
    """Return HTML for a destination card."""
    return f"""
    <div class="dest-card">
        <img src="{dest['image']}" alt="{dest['name']}">
        <div class="dest-body">
            <h3>{dest['name']}</h3>
            <p class="dest-state">{dest['state']}</p>
            <p class="dest-desc">{dest['desc']}</p>
            <div class="badges">
                <span class="badge">{dest['category']}</span>
                <span class="badge">INR {dest['budget']:,}</span>
                <span class="badge">{dest['season']}</span>
            </div>
        </div>
    </div>
    """
