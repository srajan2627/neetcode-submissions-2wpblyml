class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        charToword = {}
        wordTochar = {}

        for w, c in zip(words,pattern):
            if c in charToword and charToword[c] != w:
                return False
            if w in wordTochar and wordTochar[w] != c:
                return False
            charToword[c] = w
            wordTochar[w] = c
        
        return True