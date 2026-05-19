class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                del num_dict[num]
        
        if not num_dict:
            return -1
        else:
            return max(num_dict)
