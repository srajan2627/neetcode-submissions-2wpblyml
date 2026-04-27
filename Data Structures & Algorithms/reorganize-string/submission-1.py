class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        if len(s) < 2:
            res += s
            return res

        count = Counter(s)
        maxHeap = [(-freq,char) for char,freq in count.items()]
        heapq.heapify(maxHeap)

        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            freq,char = heapq.heappop(maxHeap)
            res += char
            freq += 1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

            if freq != 0:
                prev = (freq,char)
        return res
            
            

      
                

