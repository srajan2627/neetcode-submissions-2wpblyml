class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s.lower():
            if char.isalnum():
                clean_s += char
        
        clean_s_list = list(clean_s)

        left = 0
        right = len(clean_s_list) - 1

        while left < right:
            clean_s_list[left],clean_s_list[right] = clean_s_list[right],clean_s_list[left]
            left += 1
            right -= 1
        reversed_s = "".join(clean_s_list)
        
        return reversed_s == clean_s