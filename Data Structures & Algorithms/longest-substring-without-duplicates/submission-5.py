class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_len = 0

        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_len = max(longest_len, right - left + 1)
        return longest_len
