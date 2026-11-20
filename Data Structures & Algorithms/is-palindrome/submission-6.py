class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for letter in s:
            if letter.isalpha():
                s_list.append(letter.lower())

        left = 0
        right = len(s_list) - 1
    
        print(s_list)

        while left < right:
            if s_list[left] != s_list[right]:
                return False
            left += 1
            right -= 1
        
        return True
         
        