from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home - set income
@app.get("/", response_class=HTMLResponse)
async def get_income_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "income": data.monthly_income})

@app.post("/set_income", response_class=HTMLResponse)
async def set_income(request: Request, income: float = Form(...)):
    data.set_income(income)
    return RedirectResponse("/expenses", status_code=303)

# Expense page
@app.get("/expenses", response_class=HTMLResponse)
async def get_expense_page(request: Request):
    summary = data.get_summary()
    return templates.TemplateResponse("expenses.html", {"request": request, "summary": summary})

@app.post("/add_expense", response_class=HTMLResponse)
async def add_expense(request: Request, date: str = Form(...), category: str = Form(...), amount: float = Form(...)):
    data.add_expense(date, category, amount)
    return RedirectResponse("/expenses", status_code=303)

# Dashboard with charts & suggestions
@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    summary = data.get_summary()
    pie_html = data.category_pie_chart_html()
    bar_html = data.category_bar_chart_html()
    line_html = data.daily_cumulative_chart_html()
    suggestions = data.generate_suggestions()
    # Pass charts as safe HTML fragments
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "summary": summary,
        "pie_chart": pie_html,
        "bar_chart": bar_html,
        "line_chart": line_html,
        "suggestions": suggestions
    })
