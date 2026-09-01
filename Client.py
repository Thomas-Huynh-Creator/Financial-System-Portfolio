from Account import Account
from Branch import branch

class client:

# A client object should be able to define both personal information regarding a client, meaning first and last name,
# age, sex and probably contact details as well. Such as phone number, email address. The object should also have
# all of the relevant financial information regarding the client. This could include, account balance, account number
# Branch location.


    def __init__(self, client_name, client_number, phone_number, MembershipLvl = "Bronze"):
        self.__client_name = client_name
        self.__client_number = client_number
        self.__phone_number = phone_number
        self.__MembershipLvl = MembershipLvl
        self.__Account = []
        self.__preferred_branch = None


    def get_displayInfo_C(self,):
        return self.__client_name, self.__client_number, self.__phone_number, self.__MembershipLvl

    def __str__(self):
        return f"client name is: {self.__client_name}, Client number is : {self.__client_number}, Preferred contact method is: {self.__phone_number}"


    def __repr__(self):
            return f"client(name = {self.__client_name}, client number = {self.__client_number}, MembershipLVL = {self.__MembershipLvl}, Accounts = {self.__Account},)"

    def add_account(self, account):
        if not isinstance(account,Account):
            print("This is not a valid account")
            return
        self.__Account.append(account)
        
    def remove_account(self, account):
        if not isinstance(account,Account):
            print("This is not a valid account")
            return
        self.__Account.remove(account)

    def set_preferred_branch(self, preferred_branch):

        if not isinstance(preferred_branch, branch):
            return "This is not a valid branch"

        elif self.__preferred_branch == preferred_branch:
            return f"your preferred branch is{self.__preferred_branch}"

        self.__preferred_branch = preferred_branch

        return f"Your new branch is {self.__preferred_branch}"

    def get_preferred_branch(self):
        return self.__preferred_branch
        