class CashRegister:
    def __init__(self, discount=0):
        # Establish internal variables first to prevent attribute crashes
        self._discount = 0
        self.discount = discount
        
        # Core tracking attributes
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure it is an integer and within the 0-100 range inclusive
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        # Calculate the total for this specific item batch
        item_cost = price * quantity
        self.total += item_cost
        
        # Add item name to the items list
        self.items.append(item)
        
        # Log transaction details as an object/dictionary
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        # Guard clause: Check if there are any transactions to discount
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate percentage reduction multiplier
        multiplier = (100 - self.discount) / 100
        self.total = self.total * multiplier

    def void_last_transaction(self):
        # Safeguard against emptying an already empty array
        if not self.previous_transactions:
            return

        # Remove the last transaction record from history
        last_tx = self.previous_transactions.pop()
        
        # Deduct that specific item's cost from the total
        tx_cost = last_tx["price"] * last_tx["quantity"]
        self.total -= tx_cost
        
        # Remove the item name from the items list if it exists
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])