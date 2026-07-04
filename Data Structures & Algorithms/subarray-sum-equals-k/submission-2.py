class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        currSum = 0

        prefixSum_dict = defaultdict(int)
        prefixSum_dict[0] = 1

        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k

            if diff in prefixSum_dict:
                ans += prefixSum_dict[diff]  

            prefixSum_dict[currSum] += 1

        return ans 