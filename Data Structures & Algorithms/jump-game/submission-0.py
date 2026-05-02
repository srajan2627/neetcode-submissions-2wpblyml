class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump_index = 0

        if nums[0] == 0 and n > 1:
            return False 

        for i in range(n):
            jump_index = i + nums[i]
            if jump_index == n - 1:
                return True
        return False