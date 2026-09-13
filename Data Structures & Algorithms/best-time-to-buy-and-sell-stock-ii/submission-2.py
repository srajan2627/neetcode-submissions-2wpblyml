class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        totalProfit = 0

        while right < len(prices):
            profit = 0
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                totalProfit += profit
            left = right
            
            right += 1
        
        return totalProfit
