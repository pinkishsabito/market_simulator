from datetime import datetime, timedelta
import random

from db_repositories import SimpleOrderBook
from entities import OrderType, Order


class MarketSimulator:
    def __init__(self) -> None:
        self.order_book = SimpleOrderBook()

    def start(self, num_orders: int, match_interval: int) -> None:
        self.simulate_market(num_orders, match_interval)

    @staticmethod
    def generate_random_order(order_id: int) -> Order:
        order_type = random.choice([OrderType.BUY, OrderType.SELL])
        quantity = random.randint(1, 100)
        price = round(random.uniform(1.0, 100.0), 2)
        timestamp = datetime.now() + timedelta(seconds=random.randint(1, 60))
        return Order(order_id, order_type, quantity, price, timestamp)

    def simulate_market(self, num_orders, match_interval) -> None:
        for order_id in range(1, num_orders + 1):
            order = self.generate_random_order(order_id)
            self.order_book.add_order(order)
            if order.order_type == OrderType.BUY:
                print(f"New Buy Order: {order}")
            else:
                print(f"New Sell Order: {order}")

            if order_id % match_interval == 0:
                matched_orders = self.order_book.match_orders()
                for buy_order, sell_order, quantity in matched_orders:
                    print(f"Trade: {quantity} units at price {sell_order.price}")
