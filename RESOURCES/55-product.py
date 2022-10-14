class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent/100
        self.price -= discount


class Ebook(Product):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages