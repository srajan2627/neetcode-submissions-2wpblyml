class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for k,v in counts.items():
            if v > 1:
                return k
