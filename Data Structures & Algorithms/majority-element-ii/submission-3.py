class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        ans = []

        for num in nums:
            freq[num] += 1

        n = len(nums)

        for k,v in freq.items():
            if v > n//3:
                ans.append(k)
            
        return ans