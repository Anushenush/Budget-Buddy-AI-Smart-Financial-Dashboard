# main-Budget-Buddy-AI-Smart-Financial-Dashboard
Budget Buddy AI is a personal finance web app designed to track and analyze your daily expenses in real time.
💰 Budget Buddy AI – Smart Financial Dashboard

Elevator Pitch: “Budget Buddy AI – Your Smart Financial Coach that helps you spend wisely and save effortlessly.”

🧠 Overview

Budget Buddy AI is a web-based personal finance assistant built using FastAPI, Plotly, and Python. It allows users to enter their monthly income and add daily expenses in real-time, instantly showing:

Your total spending and remaining savings,

Visual insights through charts, and

AI-powered suggestions to improve money management.

The app’s goal is simple: 👉 Help users develop smart money habits through awareness, visualization, and intelligent advice.

🎯 Key Features

✅ Enter monthly income once per month ✅ Add daily real-time expenses (amount, category, date) ✅ Automatically calculate:

Total Expenses

Remaining Savings

Category-wise breakdown ✅ Visual dashboard with:

Pie Chart → Spending by category

Bar Graph → Expense comparison

Line Chart → Daily trend tracking ✅ AI-based Smart Advisor:

Detects overspending

Suggests how to save more

Motivates better money habits ✅ Fully offline & privacy-friendly (no login or data upload)

🧩 How It Works

Input Monthly Income You enter your monthly income at the start (e.g., ₹50,000).

Add Daily Expenses Each day, you record what you spent — e.g.,

Date: 2025-10-23

Category: Food

Amount: 250

The data is stored locally in memory.

View Dashboard Instantly visualize:

Total expenses vs income

Category-wise distribution

Daily expense trends

AI Suggestions Smart text analysis checks your spending patterns and suggests:

“Your food spending is higher than average. Try reducing it by 10% to save ₹1,200 this month.”

🖼️ Demo Preview Section Description 🏠 Home Page Enter your monthly income 🧾 Expense Entry Add expenses as they happen 📊 Dashboard Charts + Insights + AI Suggestions ⚙️ Installation Guide

Create Project Folder mkdir budget_buddy cd budget_buddy

Create and Activate Virtual Environment python -m venv venv venv\Scripts\activate # (Windows)

Install Dependencies pip install fastapi uvicorn jinja2 plotly pandas scikit-learn

Run the Application uvicorn main:app --reload

Now open: http://127.0.0.1:8000

🧰 Tech Stack Component Technology Backend FastAPI (Python) Frontend HTML, Jinja2 Templates, Plotly Charts Data In-memory Python structures (can extend to database later) AI Logic Heuristic rules for smart recommendations Style Minimal, clean UI (custom CSS) 🧠 AI Suggestion Logic

The app uses simple rule-based intelligence to analyze your expenses:

If one category > 40% of income → flagged as “overspending”

If savings < 20% → suggests cutting non-essential spending

If trend increases daily → alerts about spending rise

These rules can later evolve into a machine learning or LLM-powered model.

🌱 Future Enhancements Feature Description 🕒 Time Tracking Add specific time for each expense to analyze peak spending hours. 🛍️ Item Name Input Record exact items under each category (e.g., Lunch, Bus Ticket). 💳 Payment App Integration Connect to UPI or Paytm APIs for automatic tracking. 💬 Motivational AI Coach Give personalized tips to save and achieve goals. 📈 Savings Projection Show how small changes can increase long-term savings. 🔔 Smart Alerts Notify when spending crosses set thresholds. 💡 Why This Project Matters

Most people lose track of where their money goes — Budget Buddy AI helps them see, understand, and improve their financial habits.

It’s not just an app — it’s a financial awareness companion that teaches smart money behavior in real time.

Ideal for:

Students learning financial discipline

Families managing shared budgets

Hackathons promoting AI for social good
