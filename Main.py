from Client import client
from Account import Account
from Transaction import transaction
from Branch import branch



client_1 = client("Klein Moretti", "000000", "000000")
client_2 = client("Kyle Chopper", "666666", "666666")
client_3 = client("Zhongli", "999999", "999999")
client_4 = client("Rhoades Strauss", "888888", "888888")
 
print(f"Client Information:{client_1.displayInfo_C()}")



Account_1 = Account("000000", "Savings", "Tingen")
Account_2 = Account("111111", "Business", "Gringotts")
Account_3 = Account("222222", "Heritage", "Liyue")
Account_4 = Account("333333", "NewSaver", "Magnolia")

print(f"Account Information:{Account_2.displayInfo_A()}")

Account_2.deposit(560)
print(Account_2.balance)

Account_2.withdraw(100)

print(Account_2.balance)

Account_2.withdraw(1000)

print(Account_2.balance)

Account_2.change_branch("Liyue")

print(Account_2.bank_branch)

transaction_1 = transaction("something", "1000", "blablabla", "balling",)

transaction_1.transaction_processing("Success")


transaction_1.transaction_processing("Cancelled")


transaction_1.transaction_processing("Banana")



branch_1 = branch("696969", "Evernight", "West Tingen", "101010",)

branch_2 = branch("676767", "Siplh Co", "Verdenturf", "202020")

branch_1.branch_state_change("open")

print(branch_1.branch_avaliability)

branch_2.update_phone_number("029120")

print(client_1)

print(Account_1)

print(transaction_1)

print(branch_1)

print(repr(client_1))

print(repr(Account_1))

print(repr(transaction_1))

print(repr(branch_1))
