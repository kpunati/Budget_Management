#Developed by Karthik P. in 2023

def main_menu():
    #Display Menu
    while True:
        print("\nPersonal Budget Management Application")
        print("1. Log an Expense")
        print("2. View Reports")
        print("3. Set Budget")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            log_expense()
        elif choice == '2':
            view_reports()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
budget_data = {}
expense_data = []
expense_categories = [
    "Food",
    "Transportation",
    "Entertainment",
    "Utilities",
    "Rent",
    "Clothing",
    "Healthcare",
    "Education",
    "Other"
]

def log_expense():
    print("Log an Expense")
    
    # Display available expense categories
    print("Available Expense Categories:")
    for i, category in enumerate(expense_categories, start=1):
        print(f"{i}. {category}")
    
    # Prompt the user to select a category
    while True:
        try:
            choice = int(input("Select a category (1-9): "))
            if 1 <= choice <= len(expense_categories):
                selected_category = expense_categories[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt the user to enter the expense amount
    while True:
        try:
            expense_amount = float(input("Enter the expense amount: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Log the expense with the selected category and amount
    expense_data.append({"Category": selected_category, "Amount": expense_amount})
    print(f"Expense of ${expense_amount:.2f} logged under '{selected_category}' category.")


def view_reports():

    print("\nView Reports")
    print("1. View Data in List")
    print("2. View Data as Pandas Visualization")
    print("3. Budget Status:")

    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        # View data in a simple list
        print("\nExpense Data:")
        print()
        print("{:<15} {:<10}".format("Category", "Amount"))
        print()
        for expense in expense_data:
            print("{:<15} ${:<10.2f}".format(expense["Category"], expense["Amount"]))
    
    elif choice == '2':
       #View Data as a Bar Chart
        print("\nExpense Distribution (Text-Based Bar Chart):")
        for expense in expense_data:
            category = expense["Category"]
            amount = int(expense["Amount"])
            bar = "*" * (amount // 10)  # Adjust the scaling as needed
            print(f"{category}: {bar} ${amount:.2f}")
    elif choice == '3':
        
            print("\nBudget Status:")
    if budget_data:
        #Provide data on overall spending in context
            for category, budget in budget_data.items():
                spent = sum(expense["Amount"] for expense in expense_data if expense["Category"] == category)
                print(f"{category}: Budget ${budget:.2f} | Spent ${spent:.2f} | Remaining ${budget - spent:.2f}")
 
    else:
        print("Invalid choice. Please select a valid option.")



def set_budget():
    print("\nSet a Budget")
    
    # Display available expense categories
    print("Available Expense Categories:")
    for i, category in enumerate(expense_categories, start=1):
        print(f"{i}. {category}")

    # Prompt the user to select a category
    while True:
        try:
            choice = int(input("Select a category (1-9): "))
            if 1 <= choice <= len(expense_categories):
                selected_category = expense_categories[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt the user to enter the budget amount
    while True:
        try:
            budget_amount = float(input(f"Enter the budget amount for '{selected_category}': $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Store the budget amount for the selected category
    budget_data[selected_category] = budget_amount
    print(f"Budget of ${budget_amount:.2f} set for '{selected_category}' category.")

if __name__ == "__main__":
    main_menu()
