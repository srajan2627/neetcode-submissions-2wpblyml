class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0 
        diff = 0

        for right in range(1,len(s)):
            diff = diff + abs(ord(s[right]) - ord(s[left]))
            left += 1
        
        return diff
