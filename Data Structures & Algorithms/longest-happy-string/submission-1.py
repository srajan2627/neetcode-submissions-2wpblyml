class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ""

        for freq,char in [(-a,'a'), (-b,'b'), (-c,'c')]:

            if freq != 0:
                heapq.heappush(maxHeap,(freq,char))
        
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                freq2, char2 = heapq.heappop(maxHeap)
                res += char2
                freq2 += 1
                if freq2:
                    heapq.heappush(maxHeap,(freq2,char2))
            else:
                res += char
                freq += 1
            if freq:
                heapq.heappush(maxHeap,(freq,char))

        return res
