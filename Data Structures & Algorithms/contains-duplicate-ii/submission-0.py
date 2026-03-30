class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c_nums = {}
        for i in range(len(nums)):
            if nums[i] in c_nums and abs(i - c_nums[nums[i]]) <= k:
                return True 
            c_nums[nums[i]] = i

        return False