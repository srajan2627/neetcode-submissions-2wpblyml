class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = defaultdict(int)
        ans_arr = []
        for num in nums:
            nums_dict[num] += 1
        
        sorted_nums_dict = dict(sorted(nums_dict.items(),key = lambda item: item[1],reverse = True))
        top_k_elements = list(sorted_nums_dict)[:k]

        return top_k_elements
            