# data.py
from typing import List, Dict
import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import datetime

# In-memory storage (demo-only)
monthly_income: float = 0.0
expenses: List[Dict] = []  # each: {"date": "YYYY-MM-DD", "category": "Food", "amount": 50.0}

# ---------- Data ingestion ----------
def set_income(amount: float):
    global monthly_income
    monthly_income = float(amount)

def add_expense(date: str, category: str, amount: float):
    global expenses
    # keep date as ISO string
    try:
        # validate date
        _ = datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        # fallback to today if invalid
        date = datetime.today().strftime("%Y-%m-%d")
    expenses.append({
        "date": date,
        "category": category,
        "amount": float(amount)
    })

# ---------- Basic summaries ----------
def get_dataframe():
    if not expenses:
        return pd.DataFrame(columns=["date", "category", "amount"])
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    return df

def get_summary():
    df = get_dataframe()
    total_expense = float(df["amount"].sum()) if not df.empty else 0.0
    savings = float(monthly_income) - total_expense
    return {
        "income": float(monthly_income),
        "total_expense": total_expense,
        "savings": savings,
        "num_transactions": len(df),
        "expenses": expenses  # raw list for templates
    }

# ---------- Category-wise breakdown ----------
def category_breakdown():
    df = get_dataframe()
    if df.empty:
        return []
    cat = df.groupby("category", as_index=False)["amount"].sum().sort_values(by="amount", ascending=False)
    # return list of dicts
    return cat.to_dict(orient="records")

# ---------- Daily cumulative expenses (for line chart) ----------
def daily_cumulative_chart_html():
    df = get_dataframe()
    if df.empty:
        # return placeholder HTML
        return "<div>No expense data yet to show daily trend.</div>"
    # group by date
    daily = df.groupby(df["date"].dt.date)["amount"].sum().reset_index().sort_values("date")
    daily["cumulative"] = daily["amount"].cumsum()
    fig = px.line(daily, x="date", y="cumulative", title="Cumulative Spending Over Time", markers=True)
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

# ---------- Category pie chart ----------
def category_pie_chart_html():
    df = get_dataframe()
    if df.empty:
        return "<div>No expense data yet to show category breakdown.</div>"
    cat = df.groupby("category", as_index=False)["amount"].sum()
    fig = px.pie(cat, names="category", values="amount", title="Spending by Category")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

# ---------- Bar chart: spending per category (useful alternative) ----------
def category_bar_chart_html():
    df = get_dataframe()
    if df.empty:
        return "<div>No expense data yet to show category bar chart.</div>"
    cat = df.groupby("category", as_index=False)["amount"].sum().sort_values("amount", ascending=False)
    fig = px.bar(cat, x="category", y="amount", title="Spending per Category")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

# ---------- Simple AI-powered suggestions (heuristic rules) ----------
def generate_suggestions():
    """
    AI-powered rule-based financial coach.
    Generates dynamic, context-aware text advice.
    """
    summary = get_summary()
    income = summary["income"]
    total = summary["total_expense"]
    savings = summary["savings"]
    df = get_dataframe()
    suggestions = []

    if total == 0:
        return ["No expense data yet — add some expenses to receive personalized insights."]

    # Basic breakdown
    cat = category_breakdown()
    top_cat = cat[0] if cat else None
    avg_daily = df.groupby(df["date"].dt.date)["amount"].sum().mean()

    # ---------- Spending pattern detection ----------
    if savings < 0:
        suggestions.append(f"⚠️ You're overspending by ₹{abs(savings):.2f}. Cut discretionary items this week.")
    elif savings < income * 0.05:
        suggestions.append("⚠️ Your savings rate is below 5% of income. Try to increase savings to at least 10%.")
    elif savings > income * 0.20:
        suggestions.append("✅ Great job! You're saving more than 20% of your income — maintain this habit!")

    # Spending concentration
    for entry in cat:
        name, amt = entry["category"], float(entry["amount"])
        share = (amt / total) * 100
        if share >= 30:
            suggestions.append(f"🍔 High dependency on {name} spending ({share:.1f}% of expenses). A 15% cut here saves ₹{amt*0.15:.0f}.")
        elif share >= 15:
            suggestions.append(f"🛒 {name} takes {share:.1f}% of your expenses — moderate, but review necessity.")

    # ---------- Behavior tagging ----------
    ratio = total / income if income > 0 else 1
    if ratio > 1.1:
        behavior = "Impulsive spender"
    elif 0.8 <= ratio <= 1.1:
        behavior = "Balanced spender"
    elif ratio < 0.8 and savings > 0:
        behavior = "Conservative saver"
    else:
        behavior = "Undefined pattern"
    suggestions.append(f"💬 Spending behavior detected: {behavior}.")

    # ---------- What-if analysis ----------
    if top_cat:
        reduced = total - (top_cat["amount"] * 0.10)
        new_savings = income - reduced
        delta = new_savings - savings
        if delta > 0:
            suggestions.append(f"If you reduce '{top_cat['category']}' by 10%, you can increase savings by ₹{delta:.2f} this month.")

    # ---------- Trend prediction ----------
    if not df.empty:
        days = (df["date"].max() - df["date"].min()).days + 1
        daily_avg = total / days
        remaining_days = 30 - days if days < 30 else 0
        projected_expense = total + (daily_avg * remaining_days)
        proj_saving = income - projected_expense
        if proj_saving < 0:
            suggestions.append(f"📉 At current pace, you may overspend by ₹{abs(proj_saving):.2f} by month-end.")
        else:
            suggestions.append(f"📈 Projected month-end savings: ₹{proj_saving:.2f} if current habits continue.")

    # ---------- Generic life-hacks ----------
    life_tips = [
        "💡 Automate a monthly transfer to a savings account.",
        "📅 Review expenses every Sunday to track progress.",
        "🎯 Set a weekly mini-goal: spend 10% less on the biggest category."
    ]
    suggestions.extend(life_tips)

    return suggestions

