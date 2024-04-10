from Store import Store
from Book import Book
from Customer import Customer


#top of hierarchy, for simplicity our storeowner only handles one customer at a time
class StoreOwner():

  def __init__(self):
    self.name = ""
    self.store = Store()
    self.customer = Customer()
    self.book = Book()

  def assign_store(self, store):
    self.store = store

  def add_book_to_store(self, book):
    if (book is None or book is ''):
      raise Exception('Cannot add non-existing book to store')
    self.store.add_to_inventory(book)

  def fullfill_wishlist(self, customer):
    if (customer.wishlist_isEmpty()):
      raise Exception("Wishlist is empty")

    if (self.store.is_inventory_empty()):
      raise Exception("Store Inventory is empty")

    self.store.doTransaction(customer)

    # for book in self.store.inventory:
    #   if book in customer.wishlist:
    #     customer.remove_from_wishlist(book)
    #     self.store.remove_from_inventory(book)

    if (customer.wishlist_isEmpty() is False):
      raise Exception("Wishlist is not empty")
