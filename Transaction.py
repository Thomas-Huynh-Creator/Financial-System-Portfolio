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
        
    

    