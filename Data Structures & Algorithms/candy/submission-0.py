class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        # 1. Give every child at least 1 candy
        candies = [1] * n
        
        # 2. Left-to-Right Pass
        # Make sure children with higher ratings than their left neighbor get more candy
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # 3. Right-to-Left Pass
        # Make sure children with higher ratings than their right neighbor get more candy
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # We take the max to preserve any candies gained from the left-to-right pass
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        # 4. Return the sum of all allocated candies
        return sum(candies)