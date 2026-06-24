class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        k_rep_len = 0
        max_f = 0
        count_dict = defaultdict(int)

        for right in range(len(s)):
            count_dict[s[right]] += 1
            max_f = max(max_f,count_dict[s[right]])

            while (right - left + 1) - max_f > k:
                count_dict[s[left]] -= 1
                left += 1

            k_rep_len = max(k_rep_len,right - left + 1)
        
        return k_rep_len

