class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans= 0 
        currSum = 0

        prefixsum_dict = defaultdict(int)
        prefixsum_dict[0] = 1 

        for i in range(len(nums)):
            currSum += nums[i]

            diff = currSum - k
            if diff in prefixsum_dict:
                ans += prefixsum_dict[diff]

            prefixsum_dict[currSum] += 1

        return ans 