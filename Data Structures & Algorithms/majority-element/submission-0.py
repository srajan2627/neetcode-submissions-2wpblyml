class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        nums_dic = defaultdict(int)

        for num in nums:
            nums_dic[num] += 1
        
        for occ in nums_dic:
            if nums_dic[occ] > n:
                return occ