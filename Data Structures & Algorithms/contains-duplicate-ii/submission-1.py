class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict and abs(i - nums_dict[nums[i]]):
                return True
            nums_dict[i] = nums[i]
        return False
            