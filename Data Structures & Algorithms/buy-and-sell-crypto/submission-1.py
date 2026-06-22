class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        ans = 0

        for curr_price in range(len(prices)):
            min_price = min(min_price,prices[curr_price])
            profit = prices[curr_price] - min_price

            ans = max(ans,profit)
        
        return ans
