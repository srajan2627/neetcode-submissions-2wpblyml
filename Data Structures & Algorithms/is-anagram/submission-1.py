class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1

        for j in range(len(t)):
            t_dict[t[j]] += 1

        if s_dict == t_dict:
            return True
        else:
            return False