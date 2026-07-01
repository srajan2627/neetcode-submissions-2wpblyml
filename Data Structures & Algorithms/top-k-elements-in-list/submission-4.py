class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        while k != 0:
            num,freq = max(frequencies.items(),key = lambda x:x[1])
            ans.append(num)
            del frequencies[num]
            k -= 1
        return ans

            
                
       
            