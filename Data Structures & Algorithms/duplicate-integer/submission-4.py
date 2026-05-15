'''from collections import defaultdict()'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = defaultdict(int)

        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] += 1
        
        return False