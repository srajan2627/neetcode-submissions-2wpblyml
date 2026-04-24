class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1

        need = len(s1_count)
        for i in range(len(s2)):
            s2_count = defaultdict(int)
            curr = 0

            for j in range(i,len(s2)):
                char = s2[j]
                s2_count[char] += 1

                if s1_count[char] < s2_count[char]:
                    break
                
                if s1_count[char] == s2_count[char]:
                    curr += 1
                
                if curr == need:
                    return True
            
        return False
