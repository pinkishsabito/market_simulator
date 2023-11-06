from datetime import datetime
from enum import Enum


class OrderType(Enum):
    BUY = 1
    SELL = 2


class OrderStatus(Enum):
    OPEN = 1
    FILLED = 2
    CANCELED = 3


class Order:
    def __init__(self, order_id: int, order_type: OrderType, quantity: int, price: float, timestamp: datetime) -> None:
        self.order_id = order_id
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp
        self.status = OrderStatus.OPEN

    def __str__(self) -> str:
        return f"Order ID: {self.order_id}, Type: {self.order_type}, Quantity: {self.quantity}, Price: {self.price}, Status: {self.status}"
