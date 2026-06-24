class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        print(prefix)
        
        left = 0
        right = len(prefix) - 1
        while right - left + 1 >= 2:
            if (prefix[i] - prefix[left]) % k == 0:
                return True
            else:
                left += 1
        
        return False
