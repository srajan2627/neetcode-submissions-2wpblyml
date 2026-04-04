class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_sort = sorted(s1)

        for i in range(len(s2)):
            for j in range(i,len(s2)):
                sort_s2 = sorted(s2[i:j+1])
                if s1_sort == sort_s2:
                    return True
            
        return False
                
        
