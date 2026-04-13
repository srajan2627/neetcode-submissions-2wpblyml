class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(capacity):
            curr_load = 0
            ship = 1

            for w in weights:
                if curr_load + w > capacity:
                    curr_load = 0
                    ship += 1
                curr_load += w
            
            return ship <= days


        left = max(weights)
        right = sum(weights)



        while left <= right:
            cap = (left+right)//2
            if check(cap):
                right = cap - 1
            else:
                left = cap + 1
        
        return left
            