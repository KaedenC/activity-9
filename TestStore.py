import unittest
from Store import Store
from Book import Book


class TestStore(unittest.TestCase):

  def setUp(self):
    self.store = Store()
    self.book = Book()
    self.book.create_book("The Hobbit", "J.R.R. Tolkien", 10.99)

  def test_add_to_inventory(self):
    self.store.add_to_inventory(self.book)
    self.assertListEqual(self.store.inventory, [self.book])

  def test_add_emptybook_to_inventory(self):
    with self.assertRaises(Exception) as exception:
      self.store.add_to_inventory('')

    self.assertEqual(str(exception.exception),
                     "Cannot add empty book to inventory")

  def test_remove_from_inventory(self):
    self.store.add_to_inventory(self.book)
    self.store.remove_from_inventory(self.book)

    self.assertListEqual(self.store.inventory, [])

  def test_correctbook_removed_from_inventory(self):
    self.store.add_to_inventory(self.book)
    self.newBook = Book()
    self.newBook.create_book("the shining", "that dude", 11.99)
    self.store.add_to_inventory(self.newBook)
    self.store.remove_from_inventory(self.book)
    self.assertListEqual(self.store.inventory, [self.newBook])

  def test_remove_from_empty_inventory(self):
    with self.assertRaises(Exception) as exception:
      self.store.remove_from_inventory(self.book)

    self.assertEqual(str(exception.exception), "Inventory is empty")


if __name__ == '__main__':
  unittest.main()
