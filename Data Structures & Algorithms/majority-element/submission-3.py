class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)

        n = len(nums)

        for i in range(len(nums)):
            num_dict[nums[i]] += 1
        
        for k,v in num_dict.items():
            if v > n/2:
                return k
            