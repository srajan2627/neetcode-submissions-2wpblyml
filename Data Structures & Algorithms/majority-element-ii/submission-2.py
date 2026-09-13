class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(int)
        n = len(nums)
        res = []

        for num in nums:
            nums_dict[num] += 1
        
        for k,v in nums_dict.items():
            if v > n//3:
                res.append(k)
        
        return res