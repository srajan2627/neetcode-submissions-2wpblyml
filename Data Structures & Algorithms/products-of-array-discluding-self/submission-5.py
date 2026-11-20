class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0]*len(nums)

        ans = [0] * len(nums)
        product = 1

        for num in nums:
            if num != 0:
                product = product * num
        
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    ans[i] = product
            else:
                ans[i] = product//nums[i]

        return ans
