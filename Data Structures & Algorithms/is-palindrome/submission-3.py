class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""

        for char in s.lower():
            if char.isalnum():
                clean_s += char

        left = 0
        right = len(clean_s) - 1

        print(clean_s)

        while left <= right:
            if clean_s[left] == clean_s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True