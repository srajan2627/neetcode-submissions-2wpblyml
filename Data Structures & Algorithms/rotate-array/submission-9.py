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
        
        x = 0
        y = k
        while x < y:
            nums[x],nums[y-1] = nums[y-1],nums[x]
            x += 1
            y -= 1
        
        j = len(nums) - 1
        while k < j:
            nums[k],nums[j] = nums[j],nums[k]
            k += 1
            j -= 1
            

        

       