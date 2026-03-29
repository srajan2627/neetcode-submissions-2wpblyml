'''from collections import defaultdict()'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic_nums = defaultdict(int)

        for num in nums:

            if num in dic_nums:
                return True

            else:
                dic_nums[num] += 1
        
        return False