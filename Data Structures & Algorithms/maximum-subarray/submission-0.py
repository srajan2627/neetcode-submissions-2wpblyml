class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lar = float('-inf')
        curr = 0
        left = 0

        for right in range(len(nums)):
            curr += nums[right]
            lar = max(lar,curr)
            if curr < 0:
                curr = 0
                left = right + 1
        return lar
            



