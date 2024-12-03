from src.repository.binary_file_repository import ExpensesBinaryRepo
from src.domain.expense import Expense


class ExpenseService:
    def __init__(self, file_name: str):
        self.__repo = ExpensesBinaryRepo(file_name)

    def add_expense(self, day: int, amount: int, expense_type: str):
        """Adds a new expense."""
        if not (1 <= day <= 30):
            raise ValueError("Day must be between 1 and 30.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        expense = Expense(day, amount, expense_type)
        self.__repo.add(expense)

    def get_all_expenses(self):
        """Returns all expenses."""
        return self.__repo.get_all_expenses()

    def filter_expenses(self, min_value: int):
        """Returns expenses with an amount greater than min_value."""
        return self.__repo.filter_expenses(min_value)

    def undo_last_operation(self):
        """Undoes the last operation."""
        self.__repo.undo()
