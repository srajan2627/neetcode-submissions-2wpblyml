class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n = len(sentence1)
        m = len(sentence2)

        if n != m:
            return False
        
        i = j = 0
        pair_set = set()

        for pair in similarPairs:
            pair_set.add((pair[0], pair[1]))
            pair_set.add((pair[1], pair[0]))
        
        while i < n and j < m:
            word1 = sentence1[i]
            word2 = sentence2[j]
            if word1 != word2 and (word1, word2) not in pair_set:
                return False
            i += 1
            j += 1
        
        return True