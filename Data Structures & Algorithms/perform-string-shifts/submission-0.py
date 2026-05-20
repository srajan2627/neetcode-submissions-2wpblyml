class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = list(s)
        ans = [0] * len(s)
        
        for i in range(len(shift)):
            j = 0
            while j < len(s):
                new_index = j - shift[i][1]
                if shift[i][0] == 0:
                    ans[new_index] = s[j]
                    j+=1
                elif shift[i][0] == 1:
                    ans[new_index] = s[j]
                    j+=1
        
        return "".join(ans)

