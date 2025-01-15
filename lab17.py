class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: {amount}. Remaining balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")
        return self.__balance

    def get_account_number(self):
        return self.__account_number

account = BankAccount("123456789", 1000)
account.deposit(500)         
account.withdraw(300)           
account.get_balance()     