#SWDV 630 Week 2
class CheckingAccount:
    
    def __init__(self):
        self.balance = 0
        print("Welcome to Roszy Bank.")
        self.accountName = input("Enter your first and last name: ")
        password = input("Please enter your password: ")
        print("Welcome, ",self.accountName,", to your personal Checking Account!")
        
    def deposit(self):
        money = float(input("In US Dollars, how much money would you like to deposit? "))
        self.balance += money
        print("Deposited ",money,"US Dollars")
        
    def withdraw(self):
        money = float(input("In US Dollars, how much money would you like to withdraw? "))
        if self.balance >= money:
            self.balance -= money
            print(money,"US Dollars withdrawn.")
        else:
            print("Balance too low to withdraw that amount.")
    
    def _currentBalance(self):
        print("Current Balance of ",self.accountName,"'s Checking account is: ",self.balance,"US Dollars")
        
c = CheckingAccount()

c.deposit()
c.withdraw()
c.deposit()
c.withdraw()
c._currentBalance()