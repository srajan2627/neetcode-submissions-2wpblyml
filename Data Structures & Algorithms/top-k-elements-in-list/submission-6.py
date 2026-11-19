class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_nums = defaultdict(int)
        ans = []

        for num in nums:
            cnt_nums[num] += 1
        
        while k != 0:
            top_num = max(cnt_nums,key = cnt_nums.get)
            ans.append(top_num)
            del cnt_nums[top_num]
            k -= 1
        return ans
