import datetime
import Transaction
class TransactionService():

    def __init__(self):
        self.transactioncount = 0
        self.history = []

    def complete_transaction(self, customer, storeinventory):
        self.transactioncount += 1
        totalprice = 0
        transaction = Transaction.Transaction()

        transaction.books = customer.wishlist
        
        for item in customer.wishlist:
            if item in storeinventory:
                storeinventory.remove(item)
                totalprice += item.price
        customer.wishlist = []
        transaction.id = self.transactioncount
        transaction.customername = customer.name
        transaction.totalPrice = totalprice
        transaction.dateTime = "today"

        self.history.append(transaction)

        return storeinventory
    
