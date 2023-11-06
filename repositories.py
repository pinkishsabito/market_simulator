from abc import abstractmethod, ABC

from entities import Order


class OrderBook(ABC):
    def __init__(self) -> None:
        self.buy_orders = []
        self.sell_orders = []

    @abstractmethod
    def add_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def modify_order(self, order_id: int, new_quantity: int, new_price: float) -> None:
        pass

    @abstractmethod
    def remove_order(self, order_id: int) -> None:
        pass

    @abstractmethod
    def match_orders(self) -> list[tuple]:
        pass
