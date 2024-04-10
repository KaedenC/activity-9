import unittest
from Book import Book


class TestBook(unittest.TestCase):

  def setUp(self):
    self.book = Book()
    self.book.create_book("The Hobbit", "J.R.R. Tolkien", 10.99)

  def test_bookcreated(self):
    self.assertEqual(self.book.title, "The Hobbit")
    self.assertEqual(self.book.author, "J.R.R. Tolkien")
    self.assertEqual(self.book.price, 10.99)

if __name__ == '__main__':
  unittest.main()
