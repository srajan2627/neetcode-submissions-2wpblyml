class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left +=1
                right-=1
            
            else:
                skip_left_s = s[left+1:right+1]
                skip_right_s = s[left:right]
                return skip_left_s == skip_left_s[::-1] or skip_right_s == skip_right_s[::-1]

        return True
