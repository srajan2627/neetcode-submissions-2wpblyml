class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key = len)
        print(words)

        ans = []
        
        if len(words) == 1:
            return words

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break          
        
        return ans
            

