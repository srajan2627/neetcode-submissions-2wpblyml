class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dic = defaultdict(int)
        #char_dic = {}
        left = 0 
        res = 0
        for right in range(len(s)):
            char_dic[s[right]] += 1 

            if (right - left + 1) - max(char_dic.values()) > k:
                char_dic[s[left]] -= 1
                left += 1

            res = max(res,right - left + 1)
        return res
            
  