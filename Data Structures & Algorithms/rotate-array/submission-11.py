class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
        x = 0
        y = k - 1
        while x < y:
            nums[x],nums[y] = nums[y],nums[x]
            x += 1
            y -= 1
        
        j = len(nums) - 1
        m = k
        while m < j:
            nums[m],nums[j] = nums[j],nums[m]
            m += 1
            j -= 1