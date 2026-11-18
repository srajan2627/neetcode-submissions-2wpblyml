class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        ans = nums[0]

        for i in range(len(nums)-1):
            if count == 0:
                ans = nums[i]

            if nums[i] == nums[i+1]:
                count += 1
            else:
                count -= 1

        return ans