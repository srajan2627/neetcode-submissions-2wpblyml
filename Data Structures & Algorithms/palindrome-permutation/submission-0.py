class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        odd_count = 0

        for char in counts:
            if counts[char] % 2 != 0:
                odd_count += 1

        return odd_count <= 1
