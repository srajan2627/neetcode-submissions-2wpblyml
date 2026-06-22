class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_len = 0

        for right in range(1,len(s)):
            if s[left] == s[right] or s[right] == s[right + 1]:
                max_len = max(max_len,right - left )
                left += 1
            else:
                continue
        
        return max_len
