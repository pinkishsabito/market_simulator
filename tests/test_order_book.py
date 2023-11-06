import unittest
from order import Order, OrderType
from order_book import OrderBook


class TestOrderBook(unittest.TestCase):
    def setUp(self):
        self.order_book = OrderBook()

    def test_add_order(self):
        order = Order(order_id=1, timestamp=1.0, order_type=OrderType.BUY, quantity=10, price=100.0)
        self.order_book.add_order(order)
        self.assertEqual(len(self.order_book.buy_orders), 1)

    def test_remove_order(self):
        order = Order(order_id=1, timestamp=1.0, order_type=OrderType.BUY, quantity=10, price=100.0)
        self.order_book.add_order(order)
        self.order_book.remove_order(order.order_id)
        self.assertEqual(len(self.order_book.buy_orders), 0)

    def test_modify_order(self):
        order = Order(order_id=1, timestamp=1.0, order_type=OrderType.BUY, quantity=10, price=100.0)
        self.order_book.add_order(order)
        self.assertTrue(self.order_book.modify_order(order.order_id, 5, 110.0))
        modified_order = self.order_book.buy_orders[0]
        self.assertEqual(modified_order.quantity, 5)
        self.assertEqual(modified_order.price, 110.0)

    def test_match_orders(self):
        order1 = Order(order_id=1, timestamp=1.0, order_type=OrderType.BUY, quantity=10, price=100.0)
        order2 = Order(order_id=2, timestamp=2.0, order_type=OrderType.SELL, quantity=5, price=100.0)
        order3 = Order(order_id=3, timestamp=3.0, order_type=OrderType.BUY, quantity=7, price=99.0)

        self.order_book.add_order(order1)
        self.order_book.add_order(order2)
        self.order_book.add_order(order3)

        print("Before matching:")
        print(self.order_book.buy_orders)

        self.order_book.match_orders()  # Match orders

        print("After matching:")
        print(self.order_book.buy_orders)

        # Assert that the orders were matched correctly
        self.assertEqual(len(self.order_book.buy_orders), 2)  # One buy order remaining
        self.assertEqual(len(self.order_book.sell_orders), 0)  # No sell orders remaining


if __name__ == '__main__':
    unittest.main()
