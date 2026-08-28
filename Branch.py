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

    def __str__(self):
        return f"The branch name is: {self.branch_name}, The branch number is: {self.branch_number}, Location: {self.location}, Phone number: {self.phone_number}, branch avaliability: {self.branch_avaliability} "


    def __repr__(self):
        return f"branch(branch name = {self.branch_name}, branch availability = {self.branch_avaliability})"