class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = nums[0]
        
        for right in range(1,len(nums)):
            if nums[right] <= nums[right-1]:
                curr_sum = 0
            
            curr_sum += nums[right]
            ans = max(ans,curr_sum)

        return ans