from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # 1. Count the exact character frequencies we NEED from string 't'
        t_count = Counter(t)
        need = len(t_count) # Number of unique characters we need to satisfy
        
        # 2. Setup trackers for our sliding window
        window_count = {}
        have = 0 # Tracks how many unique characters have met their required frequency
        
        # Record for the best window: [length, left_index, right_index]
        res, min_len = [-1, -1], float("inf")
        left = 0
        
        # 3. Start expanding the right pointer
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If this character is needed, and we hit the exact frequency target, increment 'have'
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # 4. If the window is valid, try to SHRINK it from the left
            while have == need:
                # Update our result if this window is smaller than the previous minimum
                if (right - left + 1) < min_len:
                    res = [left, right]
                    min_len = right - left + 1
                
                # Pop the leftmost character out of the window
                left_char = s[left]
                window_count[left_char] -= 1
                
                # If losing this character breaks our condition, decrement 'have'
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                
                # Move left pointer inward
                left += 1
                
        # 5. Return the smallest substring found, or "" if none existed
        l, r = res
        return s[l : r + 1] if min_len != float("inf") else ""