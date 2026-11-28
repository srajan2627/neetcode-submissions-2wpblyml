class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_nums = defaultdict(int)
        ans = []

        for num in nums:
            cnt_nums[num] += 1
        
        while k != 0:
            num,freq = max(cnt_nums.items(),key = lambda x:x[1])
            ans.append(num)
            del cnt_nums[num]
            k -= 1
        return ans
