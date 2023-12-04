from bank_accounts import *

# create the bank object acounts

fason = BankAccount(10000,"Jey Fason")
maxime = BankAccount(5000,"Max King")
lebron = BankAccount(100000,"Lebron James")
sarah = BankAccount(500,"Sarah Tate")

# we have our users above like our customers with there banks name and amount or initial balance
# then we make some operation like withdraw ,deposit,transfer ..😃💲🤑

lebron.transfer(5000,fason)

lebron.get_balance()
fason.get_balance()
