from dataclasses import dataclass , field
from enum import Enum ,auto


class OrderStatus(Enum):
    """Order status"""
    OPEN = auto()
    PAID = auto()
    CANCELLED = auto()
    DELIVERED = auto()
    RETURNED = auto()

@dataclass
class Order:
    """
    list와 같은 컨테이너 타입의 빈 값을 기본값으로 받고 싶을땐 , field함수를 할당받아 사용하기
    """
    customer_id : int = 0
    customer_name : str = ""
    customer_address : str = ""
    customer_postal_code : str = ""
    customer_city : str = ""
    customer_email : str  = ""
    items: list[str] = field(default_factory=list)
    quantities: list[int] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    def create_item(self, name: str ,quantity : int , price : int ) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_stauts(self, status:OrderStatus):
        self._status = status