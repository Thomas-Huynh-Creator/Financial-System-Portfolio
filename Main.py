from Client import client
from Account import Account




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
