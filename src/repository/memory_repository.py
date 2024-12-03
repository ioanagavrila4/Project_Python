class RepositoryError(Exception):
    pass


class DuplicateIDError(RepositoryError):
    pass


class IDNotFoundError(RepositoryError):
    pass

class RepositoryIterator():
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if len(self.__data) == self.__pos:
            raise StopIteration()

        return self.__data[self.__pos]


class MemoryRepository:
    def __init__(self):
        self._data = []  # Initialize _data as a list to store expenses
        self._undo_stack = []  # Stack to store previous states of _data

    def _save_state(self):
        """Save the current state to the undo stack."""
        # Copy the data (so it doesn't reference the original list) before modifying it.
        self._undo_stack.append(self._data.copy())

    def undo(self):
        """Revert to the last saved state and print the previous state."""
        if not self._undo_stack:
            raise RepositoryError("No operations to undo.")

        # Print the last list of expenses before undoing
        self._data = self._undo_stack.pop()
        print("Last expenses before undo:")
        for expense in self._data:
            print(expense)

        # Restore the previous state from the undo stack


    def add(self, element):
        self._save_state()  # Save the state before modification
        self._data.append(element)

    def remove(self, elem_day: int):
        self._save_state()  # Save the state before modification
        # If the expense day doesn't exist, raise an error
        for i, expense in enumerate(self._data):
            if expense.day == elem_day:
                self._data.pop(i)
                return
        raise IDNotFoundError("ID not found")

    def get_all_expenses(self):
        return self._data  # Return all the expenses in the list

    def filter_expenses(self, min_value: int):
        """Filters the expenses to include only those above a certain value."""
        return [expense for expense in self._data if expense.amount > min_value]

    def __iter__(self):
        # Create an iterator for the repository
        return RepositoryIterator(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        # Access the element by index
        if item >= len(self._data):
            return None
        return self._data[item]
