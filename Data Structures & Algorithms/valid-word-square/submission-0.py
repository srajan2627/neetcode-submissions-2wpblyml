class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words):
                    return False
                
                elif i >= len(words[j]):
                    return False

                elif words[i][j] != words[j][i]:
                    return False
        
        return True


