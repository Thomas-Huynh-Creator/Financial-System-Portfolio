class Account:

    # An account object should describe the important information that would be contained inside of an account,
    # This should include account balance, account number, account type, and which bank they are with.
    # Some behaviours that could be implemented are a withdraw and a deposit feature and changing which bank they are with

    branches = ["Tingen", "Gringotts", "Verdanturf","Magnolia", "Liyue"]

    def __init__(self, account_number, account_type, bank_branch, balance = 0,):

        self.__account_number = account_number
        self.__account_type = account_type
        self.__bank_branch = bank_branch
        self.__balance = balance


    def set_deposit(self, deposit_amount,):
        if isinstance(deposit_amount, bool):
            print("Not a valid deposit")
        elif isinstance(deposit_amount, int):
            self.__balance += deposit_amount
            print("Deposited", deposit_amount)
            print("Balance is", self.__balance)
        else: 
            print("Not a valid deposit")

    def set_withdraw(self, withdraw_amount):

        if isinstance(withdraw_amount, bool):
            print("Not a valid withdraw amount")
        elif isinstance(withdraw_amount, (int, float)) and withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(" Withdrew", withdraw_amount)
            print("Current balance is", self.__balance)
            return self.__balance
        elif withdraw_amount > self.__balance:
            print("Withdraw amount greater then account balance")
        else:
            print("Not a valid withdraw amount")


    def change_branch(self, new_branch):

        if new_branch in Account.branches:
            self.__bank_branch = new_branch
        else:
            print("This branch does not exist")

    def get_displayInfo_A(self,):
        return self.__account_number, self.__account_type, self.__bank_branch, self.__balance

    def __str__(self):
        return f"The account number is: {self.__account_number}, The account type is: {self.__account_type}, and the current balance is: {self.__balance}"
    

    def __repr__(self):
        return f"account(account number = {self.__account_number}, bank branch = {self.__bank_branch}, balance = {self.__balance})"


