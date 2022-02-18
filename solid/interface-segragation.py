from abc import ABC , abstractmethod

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self , order):
        pass



class  SMSAuth:
    authorized = False

    def verify_code(self ,code):
        print(f"Verifying code {code}")
        self.authorized = True
    
    def is_atuhorized(self) -> bool:
        return self.authorized

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self , security_code , authorizer : SMSAuth) -> None:
        self.authorizer =   authorizer
        self.security_code = security_code
    
    def pay(self, order):
        if self.authorizer.is_atuhorized():
            print("Processing debit payment type")
            print(f"Verifying security code: {self.security_code}")
            order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self , security_code) -> None:
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self , security_code , authorizer : SMSAuth) -> None:
        self.authorizer =   authorizer
        self.security_code = security_code

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if self.authorizer.is_atuhorized():
            print("Processing paypal payment type")
            print(f"Using email address: {self.email_address}")
            order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorzier = SMSAuth()
processor = DebitPaymentProcessor("2349875" ,authorzier)
authorzier.verify_code()
processor.pay(order)