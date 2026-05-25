class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        count = 0

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                if s[left + 1] == s[right] and count < 2:
                    left += 1
                    count += 1
                elif s[left] == s[right - 1] and count < 2:
                    right -= 1
                    count += 1
                else:
                    return False
        
        return True
