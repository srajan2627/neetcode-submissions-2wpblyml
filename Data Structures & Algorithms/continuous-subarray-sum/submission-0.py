class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [nums[0]]

        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(len(prefix)):
            if prefix[i] % k != 0:
                continue
            else:
                return True
        
        return False