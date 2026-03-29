class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(int)

        n = len(nums)//3

        ans = []

        for num in nums:
            nums_dict[num] += 1
        
        for occ in nums_dict:
            if nums_dict[occ] > n:
                ans.append(occ)
        
        return ans
