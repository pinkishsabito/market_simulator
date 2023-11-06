# Market Simulator

The Market Simulator is a Python program that simulates a simple market where orders can be placed, modified, and matched in real-time. This program uses classes to represent orders, an order book to manage orders, and a market simulator to generate random orders and perform matching.

## Usage

To use the Market Simulator, you can follow these steps:

1. Create and initialize an `OrderBook` instance.

2. Use the `simulate_market` function to generate random orders and pass them to the order book.

3. The `simulate_market` function can also randomly modify and remove orders.

4. The `match_orders` function in the order book matches buy and sell orders based on price and quantity.

## Code Structure

- `order.py`: Defines the `Order` class and `OrderType` enum.
- `order_book.py`: Defines the `OrderBook` class, which manages buy and sell orders.
- `market_simulator.py`: Contains the `simulate_market` function for generating orders and managing the market.

## Example

```python
from order import Order, OrderType
from order_book import OrderBook
from market_simulator import simulate_market

# Create an OrderBook instance
order_book = OrderBook()

# Simulate the market with 50 random orders
simulate_market(order_book, num_orders=50, max_quantity=10, max_price=100.0)

# Orders will be added, modified, and matched based on random actions
```

## Tests
Unit tests are provided for the `OrderBook` and the market simulator. You can run the tests using `unittest`:
```batch
python -m unittest test_order_book.py
python -m unittest test_market_simulator.py
```

## Documentation
The `test_order_book.py` and `test_market_simulator.py` files contain test cases for the `OrderBook` and market simulator functionality. They ensure that orders are added, modified, and matched correctly.

Test Order Book
* `test_add_order`: Checks if an order is added to the order book correctly.
* `test_remove_order`: Verifies that an order is removed from the order book.
* `test_modify_order`: Ensures that an order is modified as expected.
* `test_match_orders`: Tests the matching of buy and sell orders.

## Test Market Simulator
* `test_simulate_market`: Verifies the behavior of the market simulator without modifications.
* `test_simulate_market_with_modifications`: Tests the simulator with order modifications and verifies the order book state.
Make sure to replace the placeholders in the tests with actual order IDs and other relevant data.

This is a simple market simulator that can serve as a starting point for more complex trading systems.