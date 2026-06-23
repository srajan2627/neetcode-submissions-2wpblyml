class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        left = 0
        right = len(s1)

        if len(s1) > len(s2):
            return False

        for char in s1:
            s1_dict[char] += 1

        for i in range(len(s1)):
            s2_dict[s2[i]] += 1

        while right < len(s2):
            if s1_dict != s2_dict:
                s2_dict[s2[right]] += 1
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1
                right += 1
            else:
                return s1_dict == s2_dict

        return s1_dict == s2_dict

        

        


            


        

        

        
            












