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

    def sort_products(self):
        self.products.sort(
            lambda product: product.price
        )