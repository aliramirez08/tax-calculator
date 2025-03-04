from tabulate import tabulate

def display_tax_table():
    """Display the tax brackets in a table format."""
    tax_brackets = [
        ["< $500", "10% (0.10)"],
        ["$500 - $1499", "15% (0.15)"],
        ["$1500 - $2499", "20% (0.20)"],
        ["$2500+", "30% (0.30)"]
    ]
    
    print("\n Weekly Income Tax Brackets:")
    print(tabulate(tax_brackets, headers=["Weekly Income", "Tax Rate"], tablefmt="grid"))

def calculate_tax(weekly_income):
    """Calculate tax withholding based on weekly income brackets."""
    if weekly_income < 500:
        tax_rate = 0.10
    elif 500 <= weekly_income < 1500:
        tax_rate = 0.15
    elif 1500 <= weekly_income < 2500:
        tax_rate = 0.20
    else:
        tax_rate = 0.30
    return weekly_income * tax_rate

# Flag to ensure tax table only shows once
first_time = True

# Loop to allow multiple calculations
while True:
    if first_time:
        display_tax_table()  # Show tax brackets only once
        first_time = False  # Prevent table from showing again

    try:
        weekly_income = float(input("\nEnter weekly income: $"))
        if weekly_income < 0:
            print("Error: Income cannot be negative.")
        else:
            print(f"Weekly Tax Withholding: ${calculate_tax(weekly_income):.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    
    # Ask user if they want to calculate again
    again = input("\nWould you like to calculate another tax withholding? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting program. Have a great day!")
        break  # Exit loop if user enters "no"
