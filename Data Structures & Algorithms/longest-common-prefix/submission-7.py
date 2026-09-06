class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for letters in strs:
            while not letters.startswith(prefix):
                prefix = prefix[:-1]
            
            if not prefix:
                return ""

        
        return prefix