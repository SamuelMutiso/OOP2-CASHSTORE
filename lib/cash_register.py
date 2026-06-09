class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        
        # Add the item name multiple times if quantity > 1
        for _ in range(quantity):
            self.items.append(item)
        
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        # The test defines "no discount to apply" when the discount percentage attribute is 0
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate reduction percentage
        multiplier = (100 - self.discount) / 100
        self.total = self.total * multiplier
        
        # Print the exact success message format required by the test
        # Note: formatting to remove trailing decimals if it's a clean int to match '$800'
        formatted_total = int(self.total) if self.total.is_integer() else round(self.total, 2)
        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_tx = self.previous_transactions.pop()
        tx_cost = last_tx["price"] * last_tx["quantity"]
        self.total -= tx_cost
        
        # Remove the item from the items list as many times as its quantity
        for _ in range(last_tx["quantity"]):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])