class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n = len(sentence1)
        m = len(sentence2)

        if n != m:
            return False
        
        i = j = 0
        pair_dict = {}

        if len(similarPairs):
            for pair in similarPairs:
                pair_dict[pair[0]] = pair[1]

            #print(pair_dict)
        
        if not len(similarPairs):
            for k in range(n):
                if sentence1[k] != sentence2[k]:
                    return False
            
        
        while i < n and j < m:
            if sentence1[i] in pair_dict.keys():
                if sentence2[j] != pair_dict[sentence1[i]]:
                    return False
            elif sentence2[j] in pair_dict.keys():
                if sentence1[i] != pair_dict[sentence2[j]]:
                    return False 
            i += 1
            j += 1
        
        return True


