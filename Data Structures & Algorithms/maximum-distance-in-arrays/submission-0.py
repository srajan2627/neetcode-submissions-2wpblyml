class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_el = float('inf')
        max_el = float('-inf')

        for i in range(len(arrays)):
            min_el = min(min_el,arrays[i][0])
            max_el = max(max_el,arrays[i][-1])

        return abs(min_el - max_el)
