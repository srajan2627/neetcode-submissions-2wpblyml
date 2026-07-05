class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_nums = len(nums) * [0]
        product = 1

        for num in nums:
            product *= num
        
        for i in range(len(product_nums)):
            product_nums[i] = product

        for j in range(len(nums)):
            product_nums[j] = int(product_nums[j]/nums[j])
        
        return product_nums