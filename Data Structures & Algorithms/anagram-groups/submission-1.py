class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        strs_dict = defaultdict(list)

        for word in strs:
            s_word = ''.join(sorted(word))
            strs_dict[s_word].append(word)
        
        for k,v in strs_dict.items():
            ans.append(v)
        return ans
            

      
