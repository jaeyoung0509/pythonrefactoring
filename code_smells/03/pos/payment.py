from typing import Protocol
from pos.order import Order
from __future__ import annotations 


class PaymentServiceConnectionError(Exception):
    """Custom error that is riased when we couldn't connect to  the payment service"""


class OrderRepository(Protocol):
    def find_order(self, order_id :str ) -> Order:
        ''''''

    def compute_order_total_price(self, order : Order) -> int:
        ''''''

class StripePaymentProcessor:
    def __init__(self) -> None:
        self.connected = False
    '''
    __future__
    __future__ 모듈에서 annotations를 import하면 파이썬 3.7에서 forward referencing이 이루어지도록 할 수 있습니다.
    여기서 forward reference 란 코드 순서상 정의되지 않은 클래스를 참조할 수 없음
    -> 이것을 해결하기 위해 annotaitons
    '''
    @staticmethod
    def create(url : str) -> StripePaymentProcessor:
        obj = StripePaymentProcessor()
        obj.connect_to_service(url)
        return obj

        

    def connect_to_service(self, url: str) -> None:
        print(f"Connecting to payment processing service at url {url}... done!")
        self.connected = True

    def process_payment(self, reference : str , price :int) -> None:
        if not self.connected:
            raise PaymentServiceConnectionError()
        print(
            f"Processing payment of ${(price / 100):.2f}, reference: {reference}."
        )