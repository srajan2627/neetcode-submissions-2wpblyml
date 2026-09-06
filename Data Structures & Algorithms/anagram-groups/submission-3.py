class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = defaultdict(list)

        for word in strs:
            s_word = "".join(sorted(word))
            dict_anagram[s_word].append(word)
        
        return list(dict_anagram.values())