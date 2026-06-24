class Solution:
    def maxScore(self, s: str) -> int:
        count_0s = 0
        count_1s = s.count('1')
        score = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                count_0s += 1
            else:
                count_1s -= 1
            score = max(score,count_0s + count_1s)
            
        return score

        

            
