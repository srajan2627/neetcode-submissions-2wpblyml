class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ship_weight = 1
        while True:
            for weight in weights:
                min_weight = 0
                min_weight += math.ceil(weight/ship_weight)
            if min_weight <= days:
                return ship_weight
            min_weight += 1
            