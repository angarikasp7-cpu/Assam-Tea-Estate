class Finances:
    def __init__(self, income=0, expenses=0):
        self.income = income
        self.expenses = expenses

    def add_income(self, amount):
        self.income += amount

    def add_expenses(self, amount):
        self.expenses += amount

    def total_profit(self):
        return self.income - self.expenses

    def __str__(self):
        return f'Income: {self.income}, Expenses: {self.expenses}, Profit: {self.total_profit()}'
