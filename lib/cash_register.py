#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - sum(item_cost for item_cost in self.items[:-1])
            self.total = last_item_price if last_item_price >= 0 else 0.0
            self.items.pop()  # Remove the last item from the items list
        else:
            print("No transactions to void.")


# Test cases
test_register = CashRegister()
test_register_with_discount = CashRegister(20)
test_register_with_discount.add_item("macbook air", 1000)
test_register_with_discount.apply_discount()
test_register_with_discount.void_last_transaction()
print(test_register_with_discount.total)      