class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            min_hours = 0
            for bananas in piles:
                min_hours += math.ceil(bananas/k)

            return min_hours <= h
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left