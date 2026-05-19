class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n = len(sentence1)
        m = len(sentence2)

        if n != m:
            return False
        
        i = j = 0

        while i < n and j < m:
            if len(similarpairs):
                if sentence1[i] != similarPairs[i][0] and sentence2[j] != similarPairs[j][1] or sentence1[i] != similarPairs[i][1] and sentence2[j] != similarPairs[j][0]:
                    return False 
                i += 1
                j += 1
            elif not len(similarpairs):
                if sentence1[i] != sentence2[j]:
                    return False
                i += 1
                j += 1
            
        return True