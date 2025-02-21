class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return (
            f"{self.name} - {self.quantity} x  {self.price} = {self.get_total_price()}"
        )


# In the Order class, we import the Product class and use it to add products to the order.
