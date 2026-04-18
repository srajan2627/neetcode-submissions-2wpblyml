class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        ans = ""
        
        for i in range(len(first)):
            if first[i] != last[i]:
                return ans 
            else:
                ans += first[i]
            
        return ans
 