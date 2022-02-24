from datetime import datetime
class Bank:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
    
    def get_balance(self):
        return f'Your balance: {self.balance} SA {datetime.now()}'
    
    def deposit(self, amount):
        if isinstance(amount, int):
            self.balance += amount
        else:
            return 'Must be number'
    
    def draw(self, amount):
        if isinstance(amount, int):
            if self.balance >= amount:
                self.balance -= amount
            else:
                return 'Sorry you do not have balance'
        else:
            return 'Must be number'

