class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = list(s)
        ans = [0] * len(s)
        
        for i in range(len(shift)):
            j = 0
            while j <= len(s)-1:

                if shift[i][0] == 0:
                    new_index = j - shift[i][1]
                    ans[new_index] = s[j]
                    j+=1

                elif shift[i][0] == 1:
                    new_index = j + shift[i][1]

                    if new_index > len(s) - 1:
                        new_index = new_index % len(s)

                    ans[new_index] = s[j]
                    j+=1
        
        return "".join(ans)

