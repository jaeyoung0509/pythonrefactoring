from pos.order import Order
from pos.system import POSSystem
from pos.line_item import LineItem
from pos.customer import Customer
def main() -> None:
    # create the POS system and setup the payment processor
    system = POSSystem()
    system.setup_payment_processor("https://api.stripe.com/v2")

    # create   a customer 
    customer = Customer("jaeyoung" , "seoul 123 123 " , "1234" ,"seoul seoul" , "jaeyoung@github.com")
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