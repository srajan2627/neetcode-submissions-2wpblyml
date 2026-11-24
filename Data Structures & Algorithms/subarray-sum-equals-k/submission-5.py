class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        currSum = 0
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0] = 1

        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k

            if diff in prefix_sum_dict:
                ans += prefix_sum_dict[diff]
            
            prefix_sum_dict[currSum] += 1
        
        return ans
