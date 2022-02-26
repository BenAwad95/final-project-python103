from datetime import datetime
class Bank:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
        self.recodes = []

    def get_balance(self):
        return f'Your balance: {self.balance} SA'
    
    def get_recode(self):
        for k, v in self.recodes:
            print(f'{k} -- {v}')
    
    def deposit(self, amount):
        if isinstance(amount, int):
            self.balance += amount
            self.recodes.append({f'Deposit {amount}': f'{amount} has been deposited to your account on {datetime.now()}'})
        else:
            return 'Must be number'
    
    def draw(self, amount):
        if isinstance(amount, int):
            if self.balance >= amount:
                self.balance -= amount
                self.recodes.append({f'Draw {amount}': f'{amount} has been drawee from your account on {datetime.now()}'})
            else:
                return 'Sorry you do not have balance'
        else:
            return 'Must be number'

