class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        count = 0

        if k == len(cardPoints):
            return sum(cardPoints)
        

        left = 0 
        right = len(cardPoints) - 1

        while left <= right and count <= k-1:
            if cardPoints[left] < cardPoints[right]:
                score += cardPoints[right]
                right -= 1
                count += 1
            elif cardPoints[left] > cardPoints[right]:
                score += cardPoints[left]
                left += 1
                count += 1
            else:
                score += cardPoints[left]
                left += 1
                right -= 1
                count += 1
        
        return score
