import pandas as pd

# Load the Excel file
file_path = 'home_budget.xlsx'
df = pd.read_excel(file_path)

# Function to update actual expenses
def update_actual(category, actual_amount):
    if category in df['Category'].values:
        df.loc[df['Category'] == category, 'Actual Amount'] = actual_amount
        df['Difference'] = df['Budgeted Amount'] - df['Actual Amount']
        df.to_excel(file_path, index=False)
        print(f"Updated {category} with actual amount: {actual_amount}")
    else:
        print(f"Category '{category}' not found.")

# Function to view the budget
def view_budget():
    print(df)

# Main menu
def display_menu():
    print("=== Home Budget Planner ===")
    print("1. View Budget")
    print("2. Update Actual Amount")
    print("3. Exit")
    print("===========================")

# Run the program
while True:
    display_menu()
    choice = input("Select an option (1-3): ")

    if choice == '1':
        view_budget()
    elif choice == '2':
        category = input("Enter the category to update: ")
        actual_amount = float(input(f"Enter the actual amount for {category}: "))
        update_actual(category, actual_amount)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")