class Book():

  def __init__(self):
    self.title = ""
    self.author = ""
    self.price = 0.0

  def create_book(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price
