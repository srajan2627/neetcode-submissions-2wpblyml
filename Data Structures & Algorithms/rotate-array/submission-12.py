class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        print(nums)
        
        left = 0
        i = k - 1

        while left < i:
            nums[left],nums[i] = nums[i],nums[left]
            left += 1
            i -= 1

        right = k
        j = len(nums) - 1

        while right < j:
            nums[right],nums[j] = nums[j],nums[right]
            right += 1
            j -= 1
        
        
