import pickle
from src.repository.memory_repository import MemoryRepository
from src.domain.expense import Expense

class ExpensesBinaryRepo(MemoryRepository):
    def __init__(self, file_name: str = "expenses.bin"):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            with open(self.__file_name, "rb") as file:
                self._data = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self._data = []

    def __save(self):
        with open(self.__file_name, "wb") as file:
            pickle.dump(self._data, file)

    def add(self, expense: Expense):
        super().add(expense)  # Use the parent class's add method
        self.__save()

    def undo(self):
        super().undo()  # Perform the undo
        self.__save()