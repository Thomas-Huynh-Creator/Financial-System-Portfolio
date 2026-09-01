from Client import client
from Account import Account
from Transaction import transaction
from Branch import branch



client_1 = client("Klein Moretti", "000000", "000000")
client_2 = client("Kyle Chopper", "666666", "666666")
client_3 = client("Zhongli", "999999", "999999")
client_4 = client("Rhoades Strauss", "888888", "888888")
 
print(f"Client Information:{client_1.get_displayInfo_C()}")



Account_1 = Account("000000", "Savings", "Tingen")
Account_2 = Account("111111", "Business", "Gringotts")
Account_3 = Account("222222", "Heritage", "Liyue")
Account_4 = Account("333333", "NewSaver", "Magnolia")

print(repr(client_1))


Account_2.change_branch("Liyue")


transaction_1 = transaction("something", "1000", "blablabla", "balling",)
transaction_2 = transaction("WestCoast", "6969", "talalalala", "falling",)

branch_1 = branch("696969", "Evernight", "West Tingen", "101010",)
branch_2 = branch("676767", "Siplh Co", "Verdenturf", "202020")

client_1.add_account(Account_1)

print(repr((client_1.set_preferred_branch(branch_2))))

branch_2.set_branch_state_change("open")

print(repr((client_1.set_preferred_branch(branch_1))))

client_1.get_preferred_branch