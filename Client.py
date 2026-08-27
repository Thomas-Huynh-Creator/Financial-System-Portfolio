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


    def displayInfo_C(self,):
        return self.client_name, self.client_number, self.phone_number, self.MembershipLvl



