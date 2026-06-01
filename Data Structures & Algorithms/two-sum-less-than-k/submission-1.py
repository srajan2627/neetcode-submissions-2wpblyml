class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1

        ans = -1

        while i < j:
            sum_nums = nums[i] + nums[j]
            if sum_nums < k:
                ans = max(ans,sum_nums)
                i += 1
            else:
                j -= 1
        return ans