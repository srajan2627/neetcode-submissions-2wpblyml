class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort_s1 = sorted(s1)
        sort_s2 = sorted(s2)

        print(sort_s1,sort_s2)

        for i in range(len(sort_s1)-1):
            if (sort_s1[i],sort_s1[i+1]) != (sort_s2[i],sort_s2[i+1]):
                return False
        
        return True