class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # 1. Create a blank array of the exact same size
        result = [0] * n
        
        # 2. Set up the two pointers at the extreme edges
        left = 0
        right = n - 1
        
        # 3. Loop backwards through the blank array's indices (e.g., 4, 3, 2, 1, 0)
        for i in range(n - 1, -1, -1):
            
            # Calculate the squares of the numbers the pointers are currently looking at
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            # 4. Compare the squares. Place the LARGER one at the end of the array.
            if left_square > right_square:
                result[i] = left_square
                left += 1       # Move the left pointer inward
            else:
                result[i] = right_square
                right -= 1      # Move the right pointer inward
                
        return result