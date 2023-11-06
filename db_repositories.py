from entities import Order, OrderType, OrderStatus
from repositories import OrderBook


class SimpleOrderBook(OrderBook):
    def add_order(self, order: Order):
        if order.order_type == OrderType.BUY:
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)

    def modify_order(self, order_id: int, new_quantity: int, new_price: float):
        for order in self.buy_orders + self.sell_orders:
            if order.order_id == order_id:
                order.quantity = new_quantity
                order.price = new_price

    def remove_order(self, order_id: int):
        self.buy_orders = [order for order in self.buy_orders if order.order_id != order_id]
        self.sell_orders = [order for order in self.sell_orders if order.order_id != order_id]

    def match_orders(self) -> list[tuple]:
        self.buy_orders.sort(key=lambda x: x.price, reverse=True)
        self.sell_orders.sort(key=lambda x: x.price)
        matched = []

        for buy_order in self.buy_orders:
            for sell_order in self.sell_orders:
                if buy_order.price >= sell_order.price:
                    quantity = min(buy_order.quantity, sell_order.quantity)
                    matched.append((buy_order, sell_order, quantity))

        for buy_order, sell_order, quantity in matched:
            if buy_order.quantity == quantity:
                self.buy_orders.remove(buy_order)
                buy_order.status = OrderStatus.FILLED
            else:
                buy_order.quantity -= quantity

            if sell_order.quantity == quantity:
                self.sell_orders.remove(sell_order)
                sell_order.status = OrderStatus.FILLED
            else:
                sell_order.quantity -= quantity

        return matched
