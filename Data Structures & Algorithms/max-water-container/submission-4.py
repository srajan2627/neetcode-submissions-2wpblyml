class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = min(heights[left],heights[right]) * (right - left)
            ans = max(ans,area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1
                left += 1
        
        return ans