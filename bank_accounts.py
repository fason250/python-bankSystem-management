import time

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,account_name):
        self.balance = initial_amount
        self.account_name = account_name
        print(f"\nAccount `{self.account_name}`\nBalance = {self.balance:.2f} Rwf\nCreated successfully👌🎉\n")
    
    def get_balance(self):
        print(f"Account `{self.account_name}`  balance = {self.balance:.2f} Rwf")
      
    def deposit(self,amount):
        self.balance += amount
        print("\nDeposit 💰 completed successfuly!🎉")
        self.get_balance()
    
    def valid_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account `{self.account_name}` has only {self.balance} Rwf 💲 deposit and try again!🙄\n"
            )
    
    def Withraw(self,amount):
        try:
            self.valid_transaction(amount)
            self.balance -= amount
            print("\nWithdraw completed 🎉 successfully!")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")
    
    def transfer(self,amount,destination_account):
        try:
            print("\n********************\n\nBeginning Transfer")
            time.sleep(5)
            self.valid_transaction(amount)
            self.Withraw(amount)
            destination_account.deposit(amount)
            print("\nTransfer completed!✅\n\n********************")
        except BalanceException as error:
            print(f"\nTransfer interrupted❌: {error}.")


class InterestRewardAccount(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete.✅✔")
        self.get_balance()


class SavingsAccount(InterestRewardAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5
    
    def Withraw(self, amount):
        try:
            self.valid_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw Completed ✅.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted❌:{error}")
