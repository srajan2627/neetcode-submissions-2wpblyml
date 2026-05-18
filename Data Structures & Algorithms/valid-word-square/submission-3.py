class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        for i in range(len(words)):
            # OPTIMIZATION: Start j at i! 
            # We only check the top-right half of the diagonal.
            for j in range(len(words[i])):
                
                # Trap A: The word is longer than the number of rows available
                if j >= len(words):
                    return False
                
                # Trap B: The mirror row we need to check is too short
                if i >= len(words[j]):
                    return False
                
                # The Mirror Check
                if words[i][j] != words[j][i]:
                    return False
                    
        return True