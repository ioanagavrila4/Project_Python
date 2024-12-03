from src.services.services import ExpenseService


class UI:
    def __init__(self, file_name: str = "expenses.pickle"):
        self.__service = ExpenseService(file_name)

    def print_menu(self):
        print("0. Exit")
        print("1. Add an expense")
        print("2. Display the list of expenses")
        print("3. Filter the list so that it contains only expenses above a certain value")
        print("4. Undo the last operation that modified program data")

    def start(self):
        while True:
            self.print_menu()
            try:
                choice = input("Your choice: ")
                if choice == "0":
                    break
                elif choice == "1":
                    self.add_expense()
                elif choice == "2":
                    self.display_expenses()
                elif choice == "3":
                    self.filter_expenses()
                elif choice == "4":
                    self.undo_last_operation()
                else:
                    print("Invalid choice!")
            except Exception as e:
                print(f"Error: {e}")

    def add_expense(self):
        """Handles adding an expense."""
        day = int(input("Please type a day (1-30): "))
        amount = int(input("Please type the amount of the expense: "))
        expense_type = input("Please type the type of the expense: ")

        self.__service.add_expense(day, amount, expense_type)
        print("Expense added successfully.")

    def display_expenses(self):
        """Displays all expenses."""
        expenses = self.__service.get_all_expenses()
        if expenses:
            for expense in expenses:
                print(expense)
        else:
            print("No expenses found.")

    def filter_expenses(self):
        """Filters expenses by value."""
        value = int(input("Please type the value to filter the results: "))
        filtered_expenses = self.__service.filter_expenses(value)
        if filtered_expenses:
            print("Filtered expenses:")
            for expense in filtered_expenses:
                print(expense)
        else:
            print(f"No expenses above the value {value}.")

    def undo_last_operation(self):
        """Handles undoing the last operation."""
        self.__service.undo_last_operation()
        print("Undo successful.")


if __name__ == "__main__":
    ui = UI()
    ui.start()
