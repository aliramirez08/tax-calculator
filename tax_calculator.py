def calculate_tax(weekly_income):
    """Calculate tax withholding based on weekly income."""
    if weekly_income < 500:
        tax_rate = 0.10
    elif 500 <= weekly_income < 1500:
        tax_rate = 0.15
    elif 1500 <= weekly_income < 2500:
        tax_rate = 0.20
    else:
        tax_rate = 0.30
    
    return weekly_income * tax_rate

def main():
    """Main function to handle user input and output."""
    try:
        weekly_income = float(input("Enter weekly income: $"))
        
        if weekly_income < 0:
            print("Error: Income cannot be negative. Please enter a valid amount.")
        else:
            tax_withholding = calculate_tax(weekly_income)
            print(f"Weekly Tax Withholding: ${tax_withholding:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
