class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        if len(s) < 2:
            res += s
            return res

        count = Counter(s)
        maxHeap = [(-freq,char) for char,freq in count.items()]
        heapq.heapify(maxHeap)

        while maxHeap:
            freq,char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == char:
                if not maxHeap:
                    break
                freq2,char2 = heapq.heappop(maxHeap)
            
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
                

