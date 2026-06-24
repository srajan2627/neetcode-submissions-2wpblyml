class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(len(nums)):
            left_sec = prefix[i]
            right_sec = prefix[-1] - prefix[i+1]
            if left_sec == right_sec:
                return i 

        return -1