class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right] and count <=1:
                left += 1
                right -= 1
            elif s[left] != s[right] and count > 1:
                return False
            else:
                count += 1
                left += 1
                right -= 1
            
        return True
            