import TransactionService as Ts

class Store():

  #inject transaction service
  def __init__(self):
    self.inventory = []
    self.TransactionService = Ts.TransactionService()

  def add_to_inventory(self, book):
    if book == None or book == '':
      raise Exception('Cannot add empty book to inventory')
    self.inventory.append(book)

  def remove_from_inventory(self, book):
    if self.is_inventory_empty():
      raise Exception("Inventory is empty")
    self.inventory.remove(book)

  def is_inventory_empty(self):
    return len(self.inventory) == 0

  def doTransaction(self, customer):
    self.inventory = self.TransactionService.complete_transaction(customer, self.inventory)