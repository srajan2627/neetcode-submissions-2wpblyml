class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        count = 0
        for num in nums:
            if num + 1 in nums:
                count += 1
        
        return count