import unittest
from Book import Book
from Customer import Customer
from Store import Store
from TransactionService import TransactionService

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.ts = TransactionService()
        self.cust = Customer()
        self.store = Store()
        self.book1 = Book()
        self.book2 = Book()

        self.book1.create_book('test', 'nobody', 1)
        self.book2.create_book('ah', 'himothy', 2)

        self.cust.add_to_wishlist(self.book1)
        self.cust.add_to_wishlist(self.book2)

        self.store.add_to_inventory(self.book1)
        self.store.add_to_inventory(self.book2)

    def test_complete_transaction(self):
        self.ts.complete_transaction(self.cust, self.store.inventory)
        self.assertEqual(self.cust.wishlist, [])
 
if __name__ == '__main__':
  unittest.main()
    