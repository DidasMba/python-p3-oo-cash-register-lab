#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0  # To keep track of the last transaction amount

    def add_item(self, title, price, quantity=1):
        # Add the item to the items list and update the total
        self.items.extend([title] * quantity)
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount

    def apply_discount(self):
        # Check if there's a discount and apply it to the total
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        # Subtract the last transaction amount from the total
        self.total -= self.last_transaction_amount
        # Reset the last transaction amount
        self.last_transaction_amount = 0

