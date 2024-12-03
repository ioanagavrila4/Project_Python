import unittest
import os
from src.domain.expense import Expense
from src.repository.binary_file_repository import ExpensesBinaryRepo

class TestExpensesBinaryRepoAdd(unittest.TestCase):
    def setUp(self):
        """Set up a test binary file for the repository."""
        self.test_file = "test_expenses.bin"
        self.repo = ExpensesBinaryRepo(self.test_file)

    def tearDown(self):
        """Clean up by deleting the test file."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_single_expense(self):
        """Test adding a single expense to the binary repository."""
        expense = Expense(2,80, "entertainment")
        self.repo.add(expense)

        # Reload the repository and check if the expense is saved
        self.repo = ExpensesBinaryRepo(self.test_file)
        self.assertEqual(len(self.repo.get_all_expenses()), 1)
        self.assertEqual(self.repo.get_all_expenses()[0], expense)

    def test_add_multiple_expenses(self):
        """Test adding multiple expenses to the binary repository."""
        expenses = [
            Expense(7, 100, "groceries"),
            Expense(20, 300, "rent"),
        ]

        for expense in expenses:
            self.repo.add(expense)

        # Reload the repository and check if all expenses are saved
        self.repo = ExpensesBinaryRepo(self.test_file)
        self.assertEqual(len(self.repo.get_all_expenses()), 2)
        self.assertEqual(self.repo.get_all_expenses(), expenses)

    def test_undo_after_add(self):
        """Test undoing after adding an expense in the binary repository."""
        expense = Expense(9, 150, "utilities")
        self.repo.add(expense)

        # Undo the addition
        self.repo.undo()

        # Reload the repository and check if the expense was undone
        self.repo = ExpensesBinaryRepo(self.test_file)
        self.assertEqual(len(self.repo.get_all_expenses()), 0)

if __name__ == "__main__":
    unittest.main()
