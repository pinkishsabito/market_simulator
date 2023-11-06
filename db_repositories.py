import heapq

from entities import Order, OrderType, OrderStatus
from repositories import OrderBook


class SimpleOrderBook(OrderBook):
    def __init__(self):
        super().__init__()
        self.buy_orders = []
        self.sell_orders = []

    @staticmethod
    def _heappush(order_list, order):
        heapq.heappush(order_list, order)

    @staticmethod
    def _heappop(order_list):
        heapq.heappop(order_list)

    def add_order(self, order: Order):
        if order.order_type == OrderType.BUY:
            self._heappush(self.buy_orders, (-order.price, order))
        else:
            self._heappush(self.sell_orders, (order.price, order))

    def modify_order(self, order_id: int, new_quantity: int, new_price: float):
        order_to_modify = None
        for order_list in [self.buy_orders, self.sell_orders]:
            for _, order in order_list:
                if order.order_id == order_id:
                    order_to_modify = order
                    break
            if order_to_modify:
                break

        if order_to_modify:
            order_to_modify.quantity = new_quantity
            order_to_modify.price = new_price

    def remove_order(self, order_id: int):
        for order_list in [self.buy_orders, self.sell_orders]:
            for i, (_, order) in enumerate(order_list):
                if order.order_id == order_id:
                    order_list.pop(i)
                    order.status = OrderStatus.CANCELED
                    break

    def match_orders(self):
        matched = []
        while self.buy_orders and self.sell_orders:
            buy_price, buy_order = self.buy_orders[0]
            sell_price, sell_order = self.sell_orders[0]

            if buy_price >= sell_price:
                quantity = min(buy_order.quantity, sell_order.quantity)
                matched.append((buy_order, sell_order, quantity))

                if buy_order.quantity == quantity:
                    self._heappop(self.buy_orders)
                    buy_order.status = OrderStatus.FILLED
                else:
                    buy_order.quantity -= quantity

                if sell_order.quantity == quantity:
                    self._heappop(self.sell_orders)
                    sell_order.status = OrderStatus.FILLED
                else:
                    sell_order.quantity -= quantity
            else:
                break

        return matched
