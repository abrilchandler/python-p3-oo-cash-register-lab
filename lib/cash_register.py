#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=[], quantity=1, last_transaction=0):
        self.discount = discount
        self.total = total
        self.items = items
        self.quantity = quantity
        self.last_transaction = last_transaction

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction = price * quantity

    

    def item_quantity(self, title, price, quantity):
        total = price * quantity
        self.total += total
        self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
           print("There is no discount to apply.")
           return 
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes tp ${self.total}.")


    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.items.pop()