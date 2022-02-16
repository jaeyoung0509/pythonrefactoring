from pos.order import Order
from pos.system import POSSystem
from pos.line_item import LineItem
from pos.customer import Customer
from pos.payment import StripePaymentProcessor
def main() -> None:
    # create the POS system and setup the payment processor
    payment_processor = StripePaymentProcessor.create("http://api.stripe.com/v2")
    system = POSSystem(payment_processor)
    # create   a customer 
    customer = Customer(
        id="jaeyoung" , 
        name="jaeyoung" , 
        postal_code="1234",
        city="seoul seoul" , 
        email="jaeyoung@github.com")
    # create the order
    order = Order(customer)
    order.add_line_item(LineItem("Keyboard", 1, 5000))
    order.add_line_item(LineItem("SSD", 1, 15000))
    order.add_line_item(LineItem("USB cable", 2, 500))

    # register and process the order
    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()