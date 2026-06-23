class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_len = 0

        left = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                longest_len = max(longest_len,right-left)
                left = right
        return longest_len
