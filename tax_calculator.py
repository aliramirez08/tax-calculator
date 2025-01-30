def calculate_tax(weekly_income):
    if weekly_income < 500:
        tax_rate = 0.10
    elif 500 <= weekly_income < 1500:
        tax_rate = 0.15
    elif 1500 <= weekly_income < 2500:
        tax_rate = 0.20
    else:
        tax_rate = 0.30

    return weekly_income * tax_rate

try:
    weekly_income = float(input("Enter weekly income: $"))
    if weekly_income < 0:
        print("Income cannot be negative.")
    else:
        print(f"Weekly Tax Withholding: ${calculate_tax(weekly_income):.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
