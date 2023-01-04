class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.length = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        check = False
        
        if account1-1 < self.length and account2-1 < self.length:
            if self.balance[account1-1] >= money:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money 
                check = True
        
        return check

    def deposit(self, account: int, money: int) -> bool:
        check = False
        if account-1 < self.length:
            self.balance[account-1] += money
            check = True
        return check

    def withdraw(self, account: int, money: int) -> bool:
        check = False
        if account-1 < self.length:
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                check = True
        
        return check


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)