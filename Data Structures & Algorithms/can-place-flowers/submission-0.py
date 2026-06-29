class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count_zero = 0
        for num in flowerbed:
            if num == 0:
                count_zero += 1
        
        if count_zero%n == 0:
            return True
        return False