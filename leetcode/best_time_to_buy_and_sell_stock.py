"""

index 0 price 7 buy 0 sell 1
index 1 price 1 buy 1 sell 1
index 2 price 5 buy 1 sell 2
index 3 price 3 buy 1 sell 2
index 4 price 6 buy 1 sell 4
index 5 price 4 buy 1 sell 4
"""
def maxProfit(prices: list[int]) -> int:
    left_bound, right_bound, profit = 0, 1, 0        
    while right_bound < len(prices):
        current_profit = prices[right_bound]-prices[left_bound]
        # If the current buy price is less than the current sell price
        if prices[left_bound] < prices[right_bound]:
            # max returns the maximum number in a list
            # is our current_profit larger than the stored profit?
            profit = max(current_profit,profit)
        else:
            # iterate the left bound index
            left_bound = right_bound
        # iterate the right bound index
        right_bound += 1            
    return profit
days = [1,7,5,7,8,9,0]
print(maxProfit(days))