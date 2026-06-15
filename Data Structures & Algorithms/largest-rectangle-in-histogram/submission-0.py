class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # Will store pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            
            # While the current height is shorter than the bar at the top of the stack
            while stack and stack[-1][1] > h:
                # Pop the taller bar
                idx, height = stack.pop()
                # Calculate the area of the rectangle formed by the popped bar
                max_area = max(max_area, height * (i - idx))
                # The current shorter bar can retroactively extend backwards to this index
                start = idx
                
            # Push the current bar with its adjusted starting index
            stack.append((start, h))
            
        # Flush out any remaining bars left in the stack
        # These bars managed to extend all the way to the end of the histogram
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
            
        return max_area