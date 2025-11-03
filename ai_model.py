def generate_suggestions(income, summary):
    suggestions = []
    total_expense = summary["total_expense"]
    savings = summary["savings"]
    categories = summary["category_breakdown"]

    # General advice
    if savings < 0:
        suggestions.append("Warning: You are overspending! Consider reducing expenses.")
    else:
        suggestions.append(f"Good job! You have saved ${savings:.2f} this month.")

    # Category suggestions
    for cat, amt in categories.items():
        percent = (amt / income) * 100
        if percent > 30:
            suggestions.append(f"High spending in {cat}: {percent:.1f}% of your income. Try reducing it.")

    return suggestions
