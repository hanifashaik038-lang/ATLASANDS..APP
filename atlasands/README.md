# ATLASANDS — Premium AI Travel Planner (India)

A multi-page Streamlit app with 12 AI features, calligraphy headings, Times New Roman body, glassmorphism UI, and only **one API key** required: OpenAI.

## 🚀 Quick start

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml and paste your OpenAI key
streamlit run app.py
```

## ☁️ Deploy on Streamlit Cloud
1. Push this folder to a GitHub repo.
2. Go to https://share.streamlit.io → New app → choose the repo.
3. Main file: `app.py`
4. **Advanced settings → Secrets** → paste:
   ```toml
   OPENAI_API_KEY = "sk-your-real-key"
   ```
5. Deploy!

## 🗂️ Structure

```
ATLASANDS/
├── app.py
├── requirements.txt
├── .gitignore
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── styles/style.css
├── data/
│   ├── destinations.py
│   ├── prompts.py
│   └── constants.py
├── utils/
│   ├── ai.py
│   ├── image_utils.py
│   ├── planner.py
│   ├── budget.py
│   └── packing.py
└── pages/
    ├── 1_AI_Assistant.py
    ├── 2_Smart_Trip_Planner.py
    ├── 3_Expense_Tracker.py
    ├── 4_Packing_Assistant.py
    ├── 5_Saved_Trips.py
    ├── 6_AI_Budget_Optimizer.py
    ├── 7_Hidden_Gems.py
    └── 8_Travel_Journal.py
```

## ✨ Features
- 12 AI tools (chat, planner, budget, packing, journal, hidden gems...)
- Calligraphy headings (Great Vibes / Dancing Script)
- Times New Roman body text
- Glassmorphism cards with hover animations
- Floating AI button
- Sidebar filters with live budget estimate
- Mobile responsive
- No 3rd-party APIs except OpenAI — high-quality Unsplash images embedded by URL (no blur)

## 🔑 Notes
- Replace any image URLs in `data/destinations.py` if you'd like your own.
- All session data (chats, expenses, saved trips) persists per browser session via `st.session_state`.
