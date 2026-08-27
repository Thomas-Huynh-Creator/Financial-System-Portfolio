class client:

# A client object should be able to define both personal information regarding a client, meaning first and last name,
# age, sex and probably contact details as well. Such as phone number, email address. The object should also have
# all of the relevant financial information regarding the client. This could include, account balance, account number
# Branch location.


    def __init__(self, client_name, client_number, phone_number, MembershipLvl = "Bronze"):
        self.client_name = client_name
        self.client_number = client_number
        self.phone_number = phone_number
        self.MembershipLvl = MembershipLvl


    def displayInfo(self,):
        return self.client_name, self.client_number, self.phone_number, self.MembershipLvl


client_1 = client("Klein Moretti", "000000", "000000")
client_2 = client("Kyle Chopper", "666666", "666666")
client_3 = client("Zhongli", "999999", "999999")
client_4 = client("Rhoades Strauss", "888888", "888888")
 
print(f"Client Information:{client_1.displayInfo()}")

class Account:

    # An account object should describe the important information that would be contained inside of an account,
    # This should include account balance, account number, account type, and which bank they are with.
    # Some behaviours that could be implemented are a withdraw and a deposit feature and changing which bank they are with


    def __init__(self, account_number, account_type, bank_branch, balance = 0,):

        self.account_number = account_number
        self.account_type = account_type
        self.bank_branch = ["Tingen", "Gringotts", "Verdanturf","Magnolia", "Liyue"]
        self.balance = balance


    def deposit(self, deposit_amount,):
        self.balance += deposit_amount
        return self.balance


    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
            return self.balance
        else:
            print("Withdraw amount larger then account balance")

    def change_branch(self, new_branch):
        self.branch = new_branch
    



Account_1 = Account("000000", "Savings",[1])
Account_2 = Account("111111", "Business", [2])
Account_3 = Account("222222", "Heritage", [5])
Account_4 = Account("333333", "NewSaver", [4])


Account_2.deposit(560)
print(Account_2.balance)

Account_2.withdraw(100)

print(Account_2.balance)

Account_2.withdraw(1000)

print(Account_2.balance)
