import random
import time
from order import Order, OrderType
from order_book import OrderBook


def simulate_market(order_books: OrderBook, num_orders: int, max_quantity: int, max_price: float):
    for _ in range(num_orders):
        order_id = random.randint(1, 1000)
        timestamp = time.time()
        order_type = random.choice([OrderType.BUY, OrderType.SELL])
        quantity = random.randint(1, max_quantity)
        price = round(random.uniform(1.0, max_price), 2)

        order = Order(order_id, timestamp, order_type, quantity, price)
        order_books.add_order(order)

        if random.random() < 0.2:
            if random.random() < 0.5:
                new_quantity = random.randint(1, max_quantity)
                new_price = round(random.uniform(1.0, max_price), 2)
                order_books.modify_order(order_id, new_quantity, new_price)
            else:
                order_books.remove_order(order_id)

        order_books.match_orders()


if __name__ == "__main__":
    order_book = OrderBook()
    simulate_market(order_book, num_orders=50, max_quantity=10, max_price=100.0)
