class Order:

    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self , name , quantitiy ,price):
        self.items.append(name)
        self.quantities.append(quantitiy)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total    

class PaymentProcessor:
    """_summary_
    """
    def pay_deibt(self  , order ,security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    def pay_credit(self  , order,security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("keyboard" , 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
processor = PaymentProcessor()
processor.pay_deibt(order ,"123123")