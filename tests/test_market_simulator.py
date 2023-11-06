import unittest

from db_repositories import SimpleOrderBook
from entities import OrderType, Order, OrderStatus


class TestSimpleOrderBook(unittest.TestCase):
    def test_add_order(self):
        order_book = SimpleOrderBook()
        order = Order(1, OrderType.BUY, 10, 50.0)
        order_book.add_order(order)
        self.assertEqual(order_book.buy_orders, [order])

    def test_modify_order(self):
        order_book = SimpleOrderBook()
        order = Order(1, OrderType.BUY, 10, 50.0)
        order_book.add_order(order)
        order_book.modify_order(1, 15, 55.0)
        self.assertEqual(order.quantity, 15)
        self.assertEqual(order.price, 55.0)

    def test_remove_order(self):
        order_book = SimpleOrderBook()
        order = Order(1, OrderType.BUY, 10, 50.0)
        order_book.add_order(order)
        order_book.remove_order(1)
        self.assertEqual(order.status, OrderStatus.CANCELED)

    def test_match_orders(self):
        order_book = SimpleOrderBook()
        buy_order = Order(1, OrderType.BUY, 10, 50.0)
        sell_order = Order(2, OrderType.SELL, 10, 45.0)
        order_book.add_order(buy_order)
        order_book.add_order(sell_order)
        matched = order_book.match_orders()
        self.assertEqual(matched, [(buy_order, sell_order, 10)])
        self.assertEqual(buy_order.status, OrderStatus.FILLED)
        self.assertEqual(sell_order.status, OrderStatus.FILLED)


if __name__ == "__main__":
    unittest.main()
