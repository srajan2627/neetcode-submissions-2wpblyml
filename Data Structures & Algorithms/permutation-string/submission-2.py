class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort_s1 = sorted(s1)
        

        for i in range(len(s2)):
            for j in range(i,len(s2)):
                j = i + 1
                s3 = s2[i:j+1]
                s3 = sorted(s3)
                if s3 == sort_s1:
                    return True
        
        return False


