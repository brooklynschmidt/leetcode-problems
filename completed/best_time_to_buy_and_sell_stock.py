class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]

        # Iterate through list and choose the lowest price
        for num in range(1, len(prices)):
            if prices[num] < price:
                price = prices[num]
            else:
                # If it's not lower than current lowest, we see if we get more profit from the newly seen number
                if profit < prices[num] - price:
                    profit = prices[num] - price
        return profit
    
