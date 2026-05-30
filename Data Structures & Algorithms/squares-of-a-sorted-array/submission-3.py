class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0 
        right = len(nums) - 1

        result = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            left_sq = nums[left]**2
            right_sq = nums[right]**2

            if left_sq > right_sq:
                result[i] = left_sq
                left += 1
            else:
                result[i] = right_sq
                right -= 1
        return result

