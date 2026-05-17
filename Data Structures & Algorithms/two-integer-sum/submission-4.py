class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums_dict:
                return [nums_dict[x],i]
            nums_dict[nums[i]] = i

        return []
            