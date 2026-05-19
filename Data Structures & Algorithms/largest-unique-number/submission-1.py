class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        unique_nums = []
        for k,v in num_dict.items():
            if v == 1:
                unique_nums.append(k)
        
        if not unique_nums:
            return -1
        else:
            return max(unique_nums)