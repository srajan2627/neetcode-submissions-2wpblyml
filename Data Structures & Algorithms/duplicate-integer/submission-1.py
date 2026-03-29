'''from collections import defaultdict()'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num = defaultdict(int)
        for num in nums:
            dict_num[num] += 1

            if dict_num[num] > 1:
                return True
    
        return False
