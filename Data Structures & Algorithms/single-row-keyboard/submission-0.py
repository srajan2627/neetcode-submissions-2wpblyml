class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dict = {}
        #keyboard = sorted(keyboard)

        for i,char in enumerate(keyboard):
            keyboard_dict[char] = i

        print(keyboard_dict)

        ans = abs(keyboard_dict[keyboard[0]] - keyboard_dict[word[0]])

        for j in range(len(word) - 1):
            ans += abs(keyboard_dict[word[j]] - keyboard_dict[word[j+1]])

        return ans
            
