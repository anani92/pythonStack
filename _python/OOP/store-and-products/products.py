import random
class Product:
  def __init__(self, name, price, category) -> None:
    self.name = name
    self.price = price
    self.category = category
    self.id = random.randrange(100, 1000)

  def update_price(self, percent_change, is_increased):
    if is_increased:
      self.price += self.price * percent_change
    else:
      self.price -= self.price * percent_change

  def print_info(self):
    print({f'product name: {self.name} price: {self.price} category: {self.category} '})
