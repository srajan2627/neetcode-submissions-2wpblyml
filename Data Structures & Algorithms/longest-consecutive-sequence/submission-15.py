class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        i = 0
        count = 1

        while i < len(nums)-1:
            if nums[i] + 1 == nums[i+1]:
                count += 1
            i += 1

        return count