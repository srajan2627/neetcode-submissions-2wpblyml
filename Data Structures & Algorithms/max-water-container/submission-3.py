class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0
        left = 0 
        right = len(heights) - 1

        while left < right:
            length = min(heights[left],heights[right])
            width = (right + 1) - (left + 1)
            area = max(area,length*width)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return area
            
        