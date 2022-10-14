class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent/100
        self.price -= discount


class Ebook(Product):
    def __init__(self, title,price, pages):
        super().__init__(title, price)
        self.pages = pages


class Cart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def total_products(self):
        return len(self.products)
    
    def subtotal(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


cart = Cart()

# adding products
cart.add_product(Product("Earbuds", 12))
cart.add_product(Product("USB Cable", 0.6))
cart.add_product(Ebook("Ikigai", 4, 196))

print(cart.subtotal())