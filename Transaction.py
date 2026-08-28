class transaction:

    transactiontypes = ["Success", "Cancelled"]

    def __init__(self, transaction_identifier, amount, description, status, transaction_type = "Pending"):
        self.transaction_identifier = transaction_identifier
        self.amount = amount
        self.description = description
        self.status = status
        self.transaction_type = transaction_type


    def transaction_processing(self, processing):
        if processing in transaction.transactiontypes:
            self.transaction_type = processing
            if processing == "Success":
                print("Transaction was a success!")
            elif processing == "Cancelled":
                print("Transaction failed!")
            else:
                print(" Invalid transaction state")

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f" Transaction Identifier: {self.transaction_identifier}, amount: {self.amount}, description: {self.description}, current status: {self.transaction_type}"
        

    def __repr__(self):
        return f"transaction(transactionID = {self.transaction_identifier}, amount = {self.amount}, status = {self.transaction_type})"

    