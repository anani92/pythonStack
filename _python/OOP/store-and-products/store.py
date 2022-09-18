from math import prod
from products import Product
class Store:
  def __init__(self, name) -> None:
    self.name = name
    self.products = []

  def add_product(self, new_product):
    print(f'added {new_product.name}')
    self.products.append(new_product)

  def sell_product(self, id):
    for product in self.products:
      if product.id == id:
        self.products.remove(product)
        print(f'sold {product.name}')


  def inflation(self, percent_increase):
    for product in self.products:
      product += percent_increase * product.price

  def set_clearance(self, category, percent_discount):
    for product in self.products:
      if product.category == category:
        product = percent_discount * product.price
  def show_products(self):
    for product in self.products:
      print(product.name, product.price)


milk = Product('milk', 5, 'dairy')
labaneh = Product('labaneh', 9, 'dairy')

milk.print_info()
anani_store = Store('ANANI')
print(milk.id)
anani_store.add_product(milk)
anani_store.add_product(labaneh)
anani_store.sell_product(735)
anani_store.show_products()

