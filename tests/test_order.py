import unittest
from order import Order, OrderType


class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        order = Order(order_id=1, timestamp=1.0, order_type=OrderType.BUY, quantity=10, price=100.0)
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.timestamp, 1.0)
        self.assertEqual(order.order_type, OrderType.BUY)
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.price, 100.0)


if __name__ == '__main__':
    unittest.main()
