class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        ans = []

        for word in strs:
            anagram_dict["".join(sorted(word))].append(word)

        for key, value in anagram_dict.items():
            ans.append(value)
        return ans
            