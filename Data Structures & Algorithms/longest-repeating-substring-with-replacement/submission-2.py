class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dic = defaultdict(int)
        #char_dic = {}
        left = 0 
        res = 0
        max_f = 0
        for right in range(len(s)):
            char_dic[s[right]] += 1 

            max_f = max(max_f,char_dic[s[right]])

            if (right - left + 1) - max_f > k:
                char_dic[s[left]] -= 1
                left += 1

            res = max(res,right - left + 1)
        return res
            
  