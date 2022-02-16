from dataclasses import dataclass , field
from enum import Enum ,auto
from line_item import LineItem
from customer import Customer

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
    customer : Customer
    items : list[LineItem] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    def add_line_item(self, item : LineItem  ) -> None:
        self.items.append(item)

    def set_stauts(self, status:OrderStatus):
        self._status = status

    @property
    def total_price(self) -> int:
        '''
        total : int = 0
        for item in self.items:
            total += item.total_price
        return total
        '''
        return sum (line_item.total_price for line_item in self.items)     