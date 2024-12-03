class Expense(object):
    def __init__(self, expense_day: int, amount_of_money: int, type: str):
        self.__day = expense_day
        self.__amount = amount_of_money
        self.__type = type

    def __eq__(self, other):
        if isinstance(other, Expense):
            return (self.day == other.day and
                    self.amount == other.amount and
                    self.type == other.type)
        return False

    def __repr__(self):
        return f"{self.day} - {self.amount} - {self.type}"
    @property
    def day(self):
        return self.__day

    @property
    def amount(self):
        return self.__amount

    @property
    def type(self):
        return self.__type


    def type_setter(self, new_value: str):
        self.__type = new_value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.day} - {self.amount} - {self.type}"

def test_expense():
    new_expense = Expense(20, 500, "permanent")
    assert new_expense.day == 20
    assert new_expense.type == "permanent"


if __name__ == "__main__":
    expense = Expense(10, 500, "permanent")
    print(expense)