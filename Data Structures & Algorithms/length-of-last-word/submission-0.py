class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_arr = s.strip().split(" ")
        last = s_arr[-1]
        print(last)
        return len(last)
