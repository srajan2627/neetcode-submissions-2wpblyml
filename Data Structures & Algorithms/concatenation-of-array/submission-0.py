class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2 * len(nums)
        ans = n * [0]
        for i in range(len(nums)):
            ans[i] = ans[i+n//2] = nums[i]

        return ans 