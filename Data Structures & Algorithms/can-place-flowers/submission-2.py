class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plants_to_plot = 0
        f = [0] + flowerbed + [0]

        for i in range(1,len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                plants_to_plot += 1
            
        return plants_to_plot >= n