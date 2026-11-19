class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] != val:
                left += 1
            else:
                right -= 1
                nums[left] = nums[right] 
        
        return left
