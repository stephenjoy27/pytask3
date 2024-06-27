import json
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Other"]
        self.filename = "expenses.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self):
        try:
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a brief description: ")
            
            print("Categories:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            
            category_index = int(input("Choose a category (enter the number): ")) - 1
            if 0 <= category_index < len(self.categories):
                category = self.categories[category_index]
            else:
                raise ValueError("Invalid category selection")

            date = datetime.now().strftime("%Y-%m-%d")
            
            expense = {
                "amount": amount,
                "description": description,
                "category": category,
                "date": date
            }
            
            self.expenses.append(expense)
            self.save_data()
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, "
                  f"Category: {expense['category']}, Description: {expense['description']}")

    def monthly_summary(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        current_month = datetime.now().strftime("%Y-%m")
        monthly_total = sum(expense['amount'] for expense in self.expenses 
                            if expense['date'].startswith(current_month))
        
        print(f"Monthly total for {current_month}: ${monthly_total:.2f}")

    def category_summary(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        category_totals = {category: 0 for category in self.categories}
        
        for expense in self.expenses:
            category_totals[expense['category']] += expense['amount']
        
        print("Category-wise expenditure:")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.monthly_summary()
            elif choice == '4':
                self.category_summary()
            elif choice == '5':
                print("Thank you for using the Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
