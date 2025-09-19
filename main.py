import matplotlib.pyplot as plt

# Categories
categories = [
    "Health", "Shopping", "Utilities", "Dining Out",
    "Transportation", "Groceries", "Entertainment", "Other"
]

def get_income():
    try:
        income = float(input("Enter your bi-weekly income: $"))
        return income
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_income()

def get_expenses():
    expenses = {}
    print("\nEnter your monthly expenses for each category:")
    for cat in categories:
        while True:
            try:
                amount = float(input(f"{cat}: $"))
                expenses[cat] = amount
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return expenses

def show_summary(income, expenses):
    total_income = income * 2  # 2 bi-weekly paychecks per month
    total_expenses = sum(expenses.values())
    savings = total_income - total_expenses

    print("\n===== Monthly Summary =====")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Savings: ${savings:.2f}")

    # Pie chart
    plt.figure(figsize=(7,7))
    plt.pie(
        expenses.values(),
        labels=expenses.keys(),
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Expense Distribution")
    plt.show()

def main():
    income = get_income()
    expenses = get_expenses()
    show_summary(income, expenses)

if __name__ == "__main__":
    main()
