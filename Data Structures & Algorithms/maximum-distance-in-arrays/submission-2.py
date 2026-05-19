class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_el = arrays[0][0]
        max_el = arrays[0][-1]

        for i in range(1,len(arrays)):
            res = max(res,abs(arrays[i][-1] - min_el),abs(max_el - arrays[i][0]))
            min_el = min(min_el,arrays[i][0])
            max_el = max(max_el,arrays[i][-1])

        return res