class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        ans = 1
        length = 1
        sort_nums = sorted(set(nums))
        print(sort_nums)

        for i in range(1,len(sort_nums)):
            if sort_nums[i-1] + 1 == sort_nums[i]:
                length += 1
                ans = max(ans,length)
            else:
                length = 1
        return ans