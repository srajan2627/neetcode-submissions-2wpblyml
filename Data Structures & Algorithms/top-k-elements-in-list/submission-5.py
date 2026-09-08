class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        for key,val in num_dict.items():
            if val >= k:
                ans.append(key)
        return ans



       
            