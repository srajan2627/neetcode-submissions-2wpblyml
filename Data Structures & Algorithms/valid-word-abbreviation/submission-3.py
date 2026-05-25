class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length = len(word)

        if word == abbr:
            return True
        
        abbr_len = 0

        i = 0

        while i < len(abbr):
            if abbr[i].isdigit() and abbr[i+1].isdigit():
                char = abbr[i]+abbr[i+1]
                x = int(char)
                abbr_len += x
                print(abbr_len)
                i += 2

            elif abbr[i].isdigit():
                x = int(abbr[i])
                abbr_len += x
                i += 1

            else:
                abbr_len += 1
                i += 1
            
            print(abbr_len)

        return length == abbr_len