'''from collections import defaultdict()'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
            #print(num_set)

        return False