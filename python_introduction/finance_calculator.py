monthly_income = float(input("Enter your monthly income "))
monthly_expenses = float(input("Enter your monthly expenses "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year with 5% interest are: ${annual_savings:.2f}")
