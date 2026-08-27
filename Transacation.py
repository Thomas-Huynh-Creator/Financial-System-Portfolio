class transacation:

    transactiontypes = ["Pending", "Success", "Cancelled"]

    def __init__(self, transaction_identifier, amount, description, status, transaction_type = "Pending"):
        self.transaction_identifier = transaction_identifier
        self.amount = amount
        self.description = description
        self.status = status
        self.transaction_type = transaction_type


    def transaction_processing(self, processing):
        if processing in transacation.transactiontype:
            

        