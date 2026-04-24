class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        ans = []
        for num in arr:
            dist = abs(num - x)
            heapq.heappush(max_heap,(-dist,-num))

        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        for num in max_heap:
            ans.append(-num[1])
        
        ans.sort()

        return ans
        