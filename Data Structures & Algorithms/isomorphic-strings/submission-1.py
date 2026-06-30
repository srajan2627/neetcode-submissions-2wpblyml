class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        i = j = 0

        while i < len(s) and j < len(t):
            s_dict[s[i]] += 1
            t_dict[t[j]] += 1

            i += 1
            j += 1

        if len(s_dict) != len(t_dict):
            return False
        
        for k in range(len(s_dict)):
            if s_dict[s[k]] != t_dict[t[k]]:
                return False
        
        return True
