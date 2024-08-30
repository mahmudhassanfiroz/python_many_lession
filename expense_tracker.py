
def add_expense(expense_list, amount, category):
    expense = {'amount': amount, 'category': category}
    expense_list.append(expense)
    print(f"Added Expense : {amount} in category: {category}")

def total_expense(expense_list):
    total = 0
    for expense in expense_list:
        total += expense['amount']
        print(f"Total Expense : {total}")
    return total

def expense_by_category(expense_list, category):
    total = 0
    for expense in expense_list:
        if expense['category'] == category:
            total += expense['amount']
            print(f"Total Expense in Category : {total}")
    return total

# expense_list = []
# expense_amount = int(input())
# expense_category = input()
# add_expense(expense_list, expense_amount, expense_category)
# print(expense_list)
# total = total_expense(expense_list)
# category_total = expense_by_category(expense_list, expense_category)
def main():
    expense_list = []
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by category")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            amount = float(input("Enter Expense Amount: "))
            category = input("Enter Expense Category: ")
            add_expense(expense_list, amount, category)
        elif choice == "2":
            total_expense(expense_list)
        elif choice == "3":
            category = input("Enter Category to view expese: ")
            expense_by_category(expense_list, category)
        elif choice == "4":
            print("Goodbye! Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.:")
    
if __name__ == "__main__":
    main()
