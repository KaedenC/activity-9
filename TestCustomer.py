import unittest
from Customer import Customer
from Book import Book


class TestCustomer(unittest.TestCase):

  def setUp(self):
    self.customer = Customer()
    self.customer.name = "Bob"
    self.customer.wishlist = []

    self.book = Book()
    self.book.create_book("The Hobbit", "J.R.R. Tolkien", 10.99)

  def test_add_to_wishlist(self):
    self.customer.add_to_wishlist(self.book)
    self.assertListEqual(self.customer.wishlist, [self.book])

  def test_add_emptybook_to_wishlist(self):
    with self.assertRaises(Exception) as exception:
      self.customer.add_to_wishlist('')

    self.assertEqual(str(exception.exception),
                     "Cannot add empty book to wishlist")

  def test_remove_from_wishlist(self):
    self.customer.add_to_wishlist(self.book)
    self.customer.remove_from_wishlist(self.book)
    self.assertListEqual(self.customer.wishlist, [])

  def test_correctbook_removed_from_wishlist(self):
    self.book2 = Book()
    self.book2.create_book("shining", "that dude", 11.99)
    self.customer.add_to_wishlist(self.book)
    self.customer.add_to_wishlist(self.book2)
    self.customer.remove_from_wishlist(self.book)
    self.assertListEqual(self.customer.wishlist, [self.book2])

  def test_remove_from_empty_wishlist(self):
    with self.assertRaises(Exception) as exception:
      self.customer.remove_from_wishlist(self.book)

    self.assertEqual(str(exception.exception), "Wishlist is empty")
    
  def test_isempty(self):
    self.assertEqual(self.customer.wishlist_isEmpty(), True)

  def test_isnotempty(self):
    self.customer.add_to_wishlist(self.book)
    self.assertEqual(self.customer.wishlist_isEmpty(), False)

if __name__ == '__main__':
  unittest.main()
