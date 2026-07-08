class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 2*n*[0]

        for i in range(len(ans)):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-n]

        return ans