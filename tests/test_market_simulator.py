import unittest

from market_simulator import simulate_market
from order_book import OrderBook


class TestMarketSimulator(unittest.TestCase):
    def test_simulate_market(self):
        order_book = OrderBook()
        simulate_market(order_book, num_orders=50, max_quantity=10, max_price=100.0)

        # Assert that the order book is not empty after simulation
        self.assertGreater(len(order_book.buy_orders), 0)
        self.assertGreater(len(order_book.sell_orders), 0)

        # Check if the total quantity of matched orders remains constant
        initial_total_buy_quantity = sum(order.quantity for order in order_book.buy_orders)
        initial_total_sell_quantity = sum(order.quantity for order in order_book.sell_orders)

        # Re-run the market simulator to match any remaining orders
        order_book.match_orders()

        # Calculate the final total quantities after matching
        final_total_buy_quantity = sum(order.quantity for order in order_book.buy_orders)
        final_total_sell_quantity = sum(order.quantity for order in order_book.sell_orders)

        # Assert that the total quantities remain the same after matching
        self.assertEqual(initial_total_buy_quantity, final_total_buy_quantity)
        self.assertEqual(initial_total_sell_quantity, final_total_sell_quantity)

    def test_simulate_market_with_modifications(self):
        order_book = OrderBook()
        simulate_market(order_book, num_orders=50, max_quantity=10, max_price=100.0)

        # Capture the initial order book state
        initial_buy_order_count = len(order_book.buy_orders)

        # Simulate modifications (add, modify, remove) on existing orders
        for _ in range(20):
            # Replace with valid order IDs from the existing orders
            order_id_to_modify = 1
            order_id_to_remove = 2

            new_quantity = 5
            new_price = 110.0

            # Modify orders
            order_book.modify_order(order_id_to_modify, new_quantity, new_price)

            # Remove orders
            order_book.remove_order(order_id_to_remove)

        # Re-run the market simulator to match any remaining orders
        order_book.match_orders()

        # Capture the final order book state
        final_buy_order_count = len(order_book.buy_orders)
        final_sell_order_count = len(order_book.sell_orders)

        # Assert that the order book state is as expected after modifications and matching
        self.assertEqual(final_buy_order_count, initial_buy_order_count)
        self.assertEqual(final_sell_order_count, 0)  # All sell orders should be matched and removed


if __name__ == '__main__':
    unittest.main()
