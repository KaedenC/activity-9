import datetime
import unittest
from StoreOwner import StoreOwner
from Store import Store
from Book import Book
from Customer import Customer
from Transaction import Transaction

class TestStoreOwner(unittest.TestCase):

  def setUp(self):
    self.customer = Customer()
    self.store = Store()
    self.storeOwner = StoreOwner()
    self.jrbook = Book()
    self.customer.name = 'the dude'
    self.jrbook.create_book("The Hobbit", "J.R.R. Tolkien", 10.99)
    self.shiningBook = Book()
    self.shiningBook.create_book("the shining", "that dude", 11.99)

    self.emptyList = []
    self.jrList = [self.jrbook]
    self.shiningList = [self.shiningBook]
    self.allbooksList = [self.jrbook, self.shiningBook]

  def test_assign_store(self):
    self.storeOwner.assign_store(self.store)
    self.assertEqual(self.storeOwner.store, self.store)

  def test_add_book_to_store(self):
    self.storeOwner.add_book_to_store(self.jrbook)

    self.assertListEqual(self.storeOwner.store.inventory, self.jrList)

  def test_add_emptybook_to_store(self):
    with self.assertRaises(Exception) as exception:
      self.storeOwner.add_book_to_store('')

    self.assertEqual(str(exception.exception),
                     "Cannot add non-existing book to store")

  def test_fulfill_wishlist(self):
    self.storeOwner.assign_store(self.store)
    self.storeOwner.add_book_to_store(self.jrbook)

    self.customer.add_to_wishlist(self.jrbook)

    #hardcodew transaction
    transaction = Transaction()
    transaction.books.append(self.jrbook)
    transaction.customername = self.customer.name
    transaction.dateTime = "today"
    transaction.totalPrice = self.jrbook.price
    transaction.id = 1

    self.storeOwner.fullfill_wishlist(self.customer)

    self.assertEqual(self.storeOwner.store.inventory, self.emptyList)
    self.assertEqual(transaction.books, self.storeOwner.store.TransactionService.history[0].books)
    self.assertEqual(transaction.customername, self.storeOwner.store.TransactionService.history[0].customername)
    self.assertEqual(transaction.id, self.storeOwner.store.TransactionService.history[0].id)
    self.assertEqual(transaction.totalPrice, self.storeOwner.store.TransactionService.history[0].totalPrice)
    self.assertEqual(transaction.dateTime, self.storeOwner.store.TransactionService.history[0].dateTime)


    # self.assertEqual(self.customer.wishlist, self.emptyList)

  def test_fulfill_wishlist_with_empty_inventory(self):
    self.storeOwner.assign_store(self.store)

    self.customer.add_to_wishlist(self.jrbook)

    with self.assertRaises(Exception) as exception:
      self.storeOwner.fullfill_wishlist(self.customer)

    self.assertEqual(str(exception.exception), "Store Inventory is empty")

  def test_fulfill_wishlist_with_empty_wishlist(self):
    self.store.inventory = []
    self.storeOwner.assign_store(self.store)

    self.storeOwner.add_book_to_store(self.jrbook)

    with self.assertRaises(Exception) as exception:
      self.storeOwner.fullfill_wishlist(self.customer)

    self.assertEqual(str(exception.exception), "Wishlist is empty")

  # def test_fulfill_part_wishlist(self):
  #   self.storeOwner.assign_store(self.store)
  #   self.storeOwner.add_book_to_store(self.jrbook)

  #   self.customer.add_to_wishlist(self.jrbook)
  #   self.customer.add_to_wishlist(self.shiningBook)

  #   with self.assertRaises(Exception) as exception:
  #     self.storeOwner.fullfill_wishlist(self.customer)

  #   self.assertEqual(str(exception.exception), "Wishlist is not empty")


if __name__ == '__main__':
  unittest.main()
