import pytest

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class ShoppingCart():
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                return
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        for item in self.items:
            if item['product'] == product:
                    if item['quantity'] <= quantity:
                        self.items.remove(item)
                    else:
                        item['quantity'] -= quantity
                    return

        raise ValueError("Product not found in the shopping cart")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

