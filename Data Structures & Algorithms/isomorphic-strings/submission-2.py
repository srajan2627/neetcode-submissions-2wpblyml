class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] in s_dict and s_dict[s[i]] != t[j]:
                return False
            if t[j] in t_dict and t_dict[t[j]] != s[i]:
                return False
            
            s_dict[s[i]] = t[j]
            t_dict[t[j]] = s[i]

            i += 1
            j += 1

        return True