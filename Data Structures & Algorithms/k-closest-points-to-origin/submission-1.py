class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        ans = []
        X1 = 0
        Y1 = 0

        for i in range(len(points)):
            dist = (X1-points[i][0])**2 + (Y1 - points[i][1])**2
            min_heap.append([dist,points[i][0],points[i][1]])
        
        heapq.heapify(min_heap)

        while k > 0:
            a,corr1,corr2 = heapq.heappop(min_heap)
            ans.append([corr1,corr2])
            k -= 1
        
        return ans

        





