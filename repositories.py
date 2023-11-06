from abc import abstractmethod, ABC

from entities import Order


class OrderBook(ABC):
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def modify_order(self, order_id: int, new_quantity: int, new_price: float):
        pass

    @abstractmethod
    def remove_order(self, order_id: int):
        pass

    @abstractmethod
    def match_orders(self):
        pass
