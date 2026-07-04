class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = defaultdict(int)
        n = len(nums)
        ans = []

        for i in range(len(nums)):
            num_dict[nums[i]] += 1
        
        for k,v in num_dict.items():
            if v > n/3:
                ans.append(k)
        
        return ans
