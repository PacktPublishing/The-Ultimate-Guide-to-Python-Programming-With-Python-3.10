class Cart:

    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)
        
    def total_products(self):
        return len(self._products)
    
    def subtotal(self):
        total = 0
        for product in self._products:
            total += product.price
        return total

    def sort_products(self):
        self._products.sort(
            lambda product: product.price
        )

    
    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        
        if self._counter < self.total_products():
            
            product = self._products[self._counter]
            
            self._counter += 1
            return product

        else:
            raise StopIteration

