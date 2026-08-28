class branch:

    branch_state = ["open", "closed"]

    def __init__(self, branch_number, branch_name, location, phone_number, branch_availability = "closed"):

        self.branch_number = branch_number
        self.branch_name = branch_name
        self.location = location
        self.phone_number = phone_number
        self.branch_avaliability = branch_availability

    def branch_state_change(self, new_state):
        if new_state in branch.branch_state:
            self.branch_avaliability = new_state
            if new_state == "open":
                print("branch is open")
            elif new_state == "closed":
                print("branch is closed")
            else:
                print("invalid branch state")

    def update_phone_number(self, new_number):
        self.phone_number = new_number
        print(f"Phone number has been changed to:{self.phone_number}")



branch_1 = branch("696969", "Evernight", "West Tingen", "101010",)

branch_2 = branch("676767", "Siplh Co", "Verdenturf", "202020")

branch_1.branch_state_change("open")

print(branch_1.branch_avaliability)

branch_2.update_phone_number("029120")