class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        nums.sort()
        res = 0

        i = 0
        count = 0
        curr = nums[0]
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                count = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            count += 1
            curr += 1 
            res = max(res,count)    
        return res