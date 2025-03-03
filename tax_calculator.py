def calculate_tax(weekly_income):
    """Calculate tax withholding based on weekly income brackets."""
    if weekly_income < 500:
        tax_rate = 0.10
    elif 500 <= weekly_income and weekly_income < 1500:
        tax_rate = 0.15
    elif 1500 <= weekly_income and weekly_income < 2500:
        tax_rate = 0.20
    else:
        tax_rate = 0.30
    return weekly_income * tax_rate

while True:  # Start a loop to repeat the program
    try:
        weekly_income = float(input("\nEnter weekly income: $"))
        if weekly_income < 0:
            print("Error: Income cannot be negative.")
        else:
            print(f"Weekly Tax Withholding: ${calculate_tax(weekly_income):.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    
    # Ask the user if they want to run the program again
    again = input("\nWould you like to calculate another tax withholding? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting program. Have a great day!")
        break  # Exit the loop if user does not enter "yes"
