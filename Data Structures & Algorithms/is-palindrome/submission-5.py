class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return s

        s_array = []

        for letter in s:
            if letter.isalnum():
                s_array.append(letter.lower())

        left = 0 
        right = len(s_array) - 1

        while left <= right:
            if s_array[left] != s_array[right]:
                return False
                
            else:
                left += 1
                right -= 1

        return True
   