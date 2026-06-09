class Solution:
    def trap(self, height: list[int]) -> int:
        # Edge case: If the array is empty, no water can be trapped
        if not height:
            return 0
        
        # 1. The Setup: Pointers at the extreme edges
        left = 0
        right = len(height) - 1
        
        # Keep track of the tallest walls seen so far from each side
        max_left = height[left]
        max_right = height[right]
        
        total_water = 0
        
        # 2. The Squeeze: Keep moving inward until the pointers meet
        while left < right:
            
            # 3. The Decision: Which side has the shorter wall? (The Bottleneck)
            if max_left < max_right:
                # The left side is the bottleneck. 
                # Move the left pointer inward and process it.
                left += 1
                
                # Update the tallest left wall if the new bar is taller
                max_left = max(max_left, height[left])
                
                # Calculate trapped water: (tallest wall - current bar height)
                total_water += max_left - height[left]
                
            else:
                # The right side is the bottleneck (or they are tied).
                # Move the right pointer inward and process it.
                right -= 1
                
                # Update the tallest right wall if the new bar is taller
                max_right = max(max_right, height[right])
                
                # Calculate trapped water: (tallest wall - current bar height)
                total_water += max_right - height[right]
                
        return total_water