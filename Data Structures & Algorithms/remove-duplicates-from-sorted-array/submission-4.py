class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                right += 1
            else:
                del nums[right]

        
        return len(nums)