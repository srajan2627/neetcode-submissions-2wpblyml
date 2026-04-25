class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        currPass = 0
        minHeap = [] # <- [end,numPass]
        for t in trips:
            numPass,start,end = t

            while minHeap and start >= minHeap[0][0]:
                currPass -= heapq.heappop(minHeap)[1]
            currPass += numPass

            if currPass > capacity:
                return False
            
            heapq.heappush(minHeap,[end,numPass])
        
        return True