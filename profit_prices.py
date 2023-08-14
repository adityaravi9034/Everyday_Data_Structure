"""You are given a list of integers representing the daily stock prices of a company. You want to maximize your profit by buying 
and selling the stock at the right time. However, you can only perform one transaction (buy one share and sell one share).
Your task is to write a function to find the maximum profit you can achieve.

Write a function max_profit(prices) that takes the list of stock prices as input and returns the maximum profit that can be achieved.

Example

prices = [7, 1, 5, 3, 6, 4]

profit = max_profit(prices)
print(profit)  # Output: 5

Explanation: In this example, the best strategy is to buy at day 2 (price = 1) and sell at day 5 (price = 6), resulting in a profit of 5."""


def max_profit(prices):
    if not prices:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print(profit)  # Output: 5
