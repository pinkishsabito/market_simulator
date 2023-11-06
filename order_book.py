from sortedcontainers import SortedList

from order import OrderType, Order


class OrderBook:
    def __init__(self):
        self.buy_orders: SortedList[Order] = SortedList(key=lambda order: (-order.price, order.timestamp))
        self.sell_orders: SortedList[Order] = SortedList(key=lambda order: (order.price, order.timestamp))
        self.order_dict = {}  # A dictionary for quick order lookup

    def add_order(self, order: Order):
        if order.order_type == OrderType.BUY:
            self.buy_orders.add(order)
        else:
            self.sell_orders.add(order)
        self.order_dict[order.order_id] = order

    def remove_order(self, order_id: int) -> bool:
        if order_id in self.order_dict:
            order = self.order_dict[order_id]
            del self.order_dict[order_id]

            # Remove the order from the respective list
            if order.order_type == OrderType.BUY:
                self.buy_orders.remove(order)
            else:
                self.sell_orders.remove(order)

            return True
        return False

    def modify_order(self, order_id: int, new_quantity: int, new_price: float) -> bool:
        if order_id in self.order_dict:
            order = self.order_dict[order_id]
            updated_order = Order(order.order_id, order.timestamp, order.order_type, new_quantity, new_price)

            # Update the order in the respective lists
            if order.order_type == OrderType.BUY:
                self.buy_orders.remove(order)
                self.buy_orders.add(updated_order)
            else:
                self.sell_orders.remove(order)
                self.sell_orders.add(updated_order)

            self.order_dict[order_id] = updated_order
            return True
        return False

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]

            if buy_order.price >= sell_order.price:
                quantity = min(buy_order.quantity, sell_order.quantity)
                print(f"Matched:")
                print(f"Buy {buy_order.quantity} at {buy_order.price}")
                print(f"Sell {sell_order.quantity} at {sell_order.price}")

                # Create updated orders with reduced quantities
                updated_buy_order = Order(buy_order.order_id, buy_order.timestamp, buy_order.order_type,
                                          buy_order.quantity - quantity, buy_order.price)
                updated_sell_order = Order(sell_order.order_id, sell_order.timestamp, sell_order.order_type,
                                           sell_order.quantity - quantity, sell_order.price)

                if updated_buy_order.quantity == 0:
                    self.remove_order(buy_order.order_id)
                else:
                    self.modify_order(buy_order.order_id, updated_buy_order.quantity, updated_buy_order.price)

                if updated_sell_order.quantity == 0:
                    self.remove_order(sell_order.order_id)
                else:
                    self.modify_order(sell_order.order_id, updated_sell_order.quantity, updated_sell_order.price)

            else:
                break
