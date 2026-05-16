class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        count = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            elif s[i] != t[j]:
                j += 1
                count += 1
        
        return count
