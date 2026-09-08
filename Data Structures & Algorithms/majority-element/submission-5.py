class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1
        
        for k,v in num_dict.items():
            if v > n/2:
                return k