class Cart:
    _instance = None

    def __new__(cls):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()

        return cls._instance


    def _init(self):
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