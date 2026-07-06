class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_nums = len(nums) * [1]

        prefix = 1

        for i in range(len(nums)):
            product_nums[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1,-1,-1):
            product_nums[i] *= suffix
            suffix *= nums[i]
        
        return product_nums