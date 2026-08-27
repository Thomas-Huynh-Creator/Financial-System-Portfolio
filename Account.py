class Account:

    # An account object should describe the important information that would be contained inside of an account,
    # This should include account balance, account number, account type, and which bank they are with.
    # Some behaviours that could be implemented are a withdraw and a deposit feature and changing which bank they are with

    branches = ["Tingen", "Gringotts", "Verdanturf","Magnolia", "Liyue"]

    def __init__(self, account_number, account_type, bank_branch, balance = 0,):

        self.account_number = account_number
        self.account_type = account_type
        self.bank_branch = bank_branch
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

        if new_branch in Account.branches:
            self.bank_branch = new_branch
        else:
            print("This branch does not exist")

    def displayInfo_A(self,):
        return self.account_number, self.account_type, self.bank_branch, self.balance
    



