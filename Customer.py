class Customer():

  def __init__(self):
    self.name = ""
    self.wishlist = []

  def add_to_wishlist(self, book):
    if (book is None or book == ''):
      raise Exception('Cannot add empty book to wishlist')
    self.wishlist.append(book)

  def remove_from_wishlist(self, book):
    if (self.wishlist_isEmpty()):
      raise Exception("Wishlist is empty")
    self.wishlist.remove(book)

  def wishlist_isEmpty(self):
    return len(self.wishlist) == 0
