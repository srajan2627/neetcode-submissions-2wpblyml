class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_nums_dict = defaultdict(int)
        prefix_nums_dict[0] = 1

        ans = curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i] 
            diff = curr_sum - k


            if diff in prefix_nums_dict:
                ans += prefix_nums_dict[diff]

            prefix_nums_dict[curr_sum] += 1
            
        return ans