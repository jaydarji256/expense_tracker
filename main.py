import pandas as pd
from tabulate import tabulate
import os

FILENAME = "expenses.csv"

if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    df.to_csv(FILENAME, index=False)

#adding expense
def add_expense():
    date = input("📅 Enter date (YYYY-MM-DD): ")
    category = input("📂 Enter category (Food, Travel, etc.): ")
    try:
        amount = float(input("💰 Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return
    note = input("📝 Add a note (optional): ")

    df = pd.read_csv(FILENAME)
    new_row = pd.DataFrame([[date, category, amount, note]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILENAME, index=False)
    print("✅ Expense added!\n")

#view expense
def view_expenses():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("📭 No expenses to show.")
    else:
        print(tabulate(df, headers="keys", tablefmt="grid"))

#delete expense
def delete_expense():
    view_expenses()
    try:
        idx = int(input("🗑️ Enter row index to delete: "))
        df = pd.read_csv(FILENAME)
        df.drop(idx, inplace=True)
        df.to_csv(FILENAME, index=False)
        print("✅ Expense deleted.\n")
    except:
        print("❌ Invalid index.")

#main_menu
def main_menu():
    while True:
        print("\n=== 💼 Personal Expense Tracker ===")
        print("1. ➕ Add Expense")
        print("2. 📄 View Expenses")
        print("3. ❌ Delete Expense")
        print("4. 🚪 Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()