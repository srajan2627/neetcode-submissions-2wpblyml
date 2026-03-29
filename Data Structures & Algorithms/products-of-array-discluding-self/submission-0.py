class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        post_prod = [0] * len(nums)
        ans = [0] * len(nums)

        prefix_prod[0] = 1
        post_prod[len(nums)-1] = 1

        for i in range(1,len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            post_prod[i] = post_prod[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            ans[i] = prefix_prod[i] * post_prod[i]
        
        return ans


