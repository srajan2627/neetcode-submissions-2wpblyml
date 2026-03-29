class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_colored_index = i
            
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_colored_index]:
                    min_colored_index = j
                
            nums[min_colored_index],nums[i] = nums[i],nums[min_colored_index]