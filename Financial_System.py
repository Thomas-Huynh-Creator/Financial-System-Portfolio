class client:
    def __init__(self, client_name, client_number, phone_number, MembershipLvl):
        self.client_name = client_name
        self.client_number = client_number
        self.phone_number = phone_number


    def displayInfo(self, client_name, client_number, phone_number, MembershipLvl):
        return client_name, client_number, phone_number, MembershipLvl


client = client()
print(f"Client Information:{client.displayInfo}")


class Account:
    def __init__(self, account_number, account_type, bank_branch, balance = 0,):

        self.account_number = account_number
        self.account_type = account_type
        self.bank_branch = ["Tingen", "Gringotts", "Verdanturf",]


def deposit(self, deposit_amount, balance):
    balance += deposit_amount
    return balance


def withdraw(self, balance, withdraw_amount):
    if withdraw_amount < balance:
        balance -= withdraw_amount
        return balance
    else:
        print("Withdraw amount larger then account balance")

def change_branch(self, new_branch):
    self.branch = new_branch
    
  





