class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = nums[0]
        globMin = nums[0]
        currmin = 0
        currmax = 0
        total = 0

        for num in nums:
            currmax = max(currmax + num,num)
            currmin = min(currmin + num,num)
            globMax = max(globMax,currmax)
            globMin = min(globMin,currmin)
            total += num
        
        if globMax > 0:
            return total - globMin
        else:
            return globMax