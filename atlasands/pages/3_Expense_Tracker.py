# pages/3_Expense_Tracker.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.image_utils import load_css

st.set_page_config(page_title="Expense Tracker · ATLASANDS", page_icon="💰", layout="wide")
load_css()

st.markdown(
    "<div class='section-title'><h2>Expense Tracker</h2>"
    "<div class='sub'>See every rupee. Stay in control. Travel smart.</div></div>",
    unsafe_allow_html=True,
)

if "expenses" not in st.session_state:
    st.session_state.expenses = []

budget = st.number_input("Total Trip Budget (INR)", 1000, 1_000_000, 25000, 500)

with st.form("add_expense", clear_on_submit=True):
    c1, c2, c3 = st.columns(3)
    cat = c1.selectbox("Category", ["Travel", "Food", "Stay", "Activities", "Shopping", "Other"])
    amt = c2.number_input("Amount (INR)", 0, 200000, 500)
    note = c3.text_input("Note (optional)")
    add = st.form_submit_button("➕ Add Expense")
    if add:
        st.session_state.expenses.append({"Category": cat, "Amount": amt, "Note": note})

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    spent = int(df["Amount"].sum())
    remaining = max(0, budget - spent)

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Spent", f"INR {spent:,}")
    c2.metric("Remaining", f"INR {remaining:,}")
    c3.metric("Budget", f"INR {budget:,}")

    pct = min(spent / budget, 1.0) if budget else 0
    st.progress(pct)

    if spent > budget:
        st.error(f"⚠️ Over budget by INR {spent - budget:,}!")
    elif pct > 0.8:
        st.warning("You've used over 80% of your budget. Spend wisely!")
    else:
        st.success("You're on track. Enjoy the journey!")

    fig = px.pie(df, names="Category", values="Amount",
                 title="Spending Breakdown", hole=0.45,
                 color_discrete_sequence=px.colors.sequential.Oranges_r)
    fig.update_layout(font_family="Times New Roman",
                      title_font_family="Dancing Script",
                      title_font_size=28,
                      paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)

    if st.button("🗑️ Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()
else:
    st.info("Add your first expense above to start tracking.")
