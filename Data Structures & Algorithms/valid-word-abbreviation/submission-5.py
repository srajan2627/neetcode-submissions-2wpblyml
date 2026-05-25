class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        char = ''

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1

            elif abbr[j].isalpha():
                return False
            
            else:
                while abbr[j].isdigit():
                    char += abbr[j]
                    j += 1
                i += int(char)

        return i == len(word) and j == len(abbr)
