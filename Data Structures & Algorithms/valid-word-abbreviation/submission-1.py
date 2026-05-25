class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length = len(word)

        if word == abbr:
            return True
        
        abbr_len = 0

        for char in abbr:
            if char.isdigit():
                x = int(char)
                abbr_len += x
            else:
                abbr_len += 1

        return length == abbr_len