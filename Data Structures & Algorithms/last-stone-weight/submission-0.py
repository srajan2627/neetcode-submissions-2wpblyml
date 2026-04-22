class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-weight for weight in stones]

        heapq.heapify(weights)

        while len(weights) > 1:
            x = -heapq.heappop(weights)
            y = -heapq.heappop(weights)

            if x != y:
                heapq.heappush(weights,-abs(x-y))
            
        if weights:
            return -weights[0]
        else:
            return 0