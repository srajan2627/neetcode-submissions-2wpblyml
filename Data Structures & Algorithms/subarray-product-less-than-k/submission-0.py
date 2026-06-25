class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left, right = 0,0
        ans = 0

        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product = product//nums[left]
                left += 1
            
            ans += right - left + 1
            right += 1
        
        return ans
                
