class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0: 
                return 0
            left, right = 0, 0
            ans = 0
            subarray_total = 0

            while right < len(nums):
                subarray_total += nums[right]
                while subarray_total > k:
                    subarray_total -= nums[left]
                    left += 1

                ans += right - left + 1
                right += 1
            
            return ans

        return atMost(goal) - atMost(goal - 1)