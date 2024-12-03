from src.domain.expense import Expense

class ExpensesTextFileRepo:
    def __init__(self, file_name: str = "expenses.txt"):
        self.__file_name = file_name
        self._data = []  # Internal list to store Expense objects
        self.__load()

    def __load(self):
        """Load expenses from the text file."""
        self._data = []
        try:
            with open(self.__file_name, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        day, amount, expense_type = parts
                        expense = Expense(int(day), int(amount), expense_type)
                        self._data.append(expense)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty list
            self._data = []

    def __save(self):
        """Save all expenses to the text file."""
        with open(self.__file_name, "w") as file:
            for expense in self._data:
                file.write(f"{expense.day},{expense.amount},{expense.type}\n")

    def add(self, expense: Expense):
        """Add a new expense and save it to the file."""
        self._data.append(expense)
        self.__save()

    def get_all_expenses(self):
        """Return a list of all expenses."""
        return self._data

    def filter_expenses(self, min_value: int):
        """Filter expenses above a certain value."""
        return [expense for expense in self._data if expense.amount > min_value]

