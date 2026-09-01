
class branch:

    branch_state = ["open", "closed"]

    def __init__(self, branch_number, branch_name, location, phone_number, branch_availability = "closed"):

        self.__branch_number = branch_number
        self.__branch_name = branch_name
        self.__location = location
        self.__phone_number = phone_number
        self.__branch_avaliability = branch_availability

    def set_branch_state_change(self, new_state):
        if isinstance(new_state, str):
            if new_state in branch.branch_state:
                self.__branch_avaliability = new_state
                if new_state == "open":
                    print("branch is open")
                elif new_state == "closed":
                    print("branch is closed")
            else:
                print("Invalid branch state")
        else:
            print("invalid branch state")

    def set_update_phone_number(self, new_number):
        if isinstance(new_number, int):
            self.__phone_number = new_number
            print(f"Phone number has been changed to:{self.__phone_number}")
        else: 
            print("Invalid Phone number")
    def __str__(self):
        return f"The branch name is: {self.__branch_name}, The branch number is: {self.__branch_number}, Location: {self.__location}, Phone number: {self.__phone_number}, branch avaliability: {self.__branch_avaliability} "


    def __repr__(self):
        return f"branch(branch name = {self.__branch_name}, branch availability = {self.__branch_avaliability})"


            