class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        count = 0

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                skip_left_char = s[left+1:right+1]
                skip_right_char = s[left:right]

                return skip_left_char == skip_left_char[::-1] or skip_right_char == skip_right_char[::-1]
                
        
        return True
