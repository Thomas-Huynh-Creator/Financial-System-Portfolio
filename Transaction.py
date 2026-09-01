class transaction:

    transactiontypes = ["Success", "Cancelled"]

    def __init__(self, transaction_identifier, amount, description, status, transaction_type = "Pending"):
        self.__transaction_identifier = transaction_identifier
        self.__amount = amount
        self.__description = description
        self.__status = status
        self.__transaction_type = transaction_type


    def transaction_processing(self, processing):
        if processing in transaction.transactiontypes:
            self.__transaction_type = processing
            if processing == "Success":
                print("Transaction was a success!")
            elif processing == "Cancelled":
                print("Transaction failed!")
            else:
                print(" Invalid transaction state")

    def set_update_description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
            print(" Description Updated to:", new_description)
        else:
            print("Invalid Input")


    def __str__(self):
        return f" Transaction Identifier: {self.__transaction_identifier}, amount: {self.__amount}, description: {self.__description}, current status: {self.__transaction_type}"
        

    def __repr__(self):
        return f"transaction(transactionID = {self.__transaction_identifier}, amount = {self.__amount}, status = {self.__transaction_type})"

    