import pickle
from src.domain.expense import Expense

# Create a list of sample Expense objects
expenses = [
    Expense(10, 140, "permanent"),
    Expense(11, 75, "temporary"),
    Expense(12, 200, "other"),
]

# Save the list to a binary file
with open("expenses.pickle", "wb") as file:
    pickle.dump(expenses, file)

print("expenses.pickle has been created with sample data.")
