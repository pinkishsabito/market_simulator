from enum import Enum
from typing import NamedTuple


class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"


class Order(NamedTuple):
    order_id: int
    timestamp: float
    order_type: OrderType
    quantity: int
    price: float
