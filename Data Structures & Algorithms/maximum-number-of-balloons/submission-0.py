class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        str_dict = {'b': 1,
                    'a':1,
                    'l':2,
                    'o':2,
                    'n':1}
        
        text_dict = defaultdict(int)
        for letter in text:
            if letter in str_dict:
                text_dict[letter] += 1
        
        res = len(text)
        for l in str_dict.keys():
            res = min(res, text_dict[l] // str_dict[l])
        return res