class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        right = len(people) - 1
        count = 0

        while left <= right:
            rem_weight = limit - people[right] 
            count += 1
            right -= 1

            if left <= right and rem_weight >= people[left]:
                left += 1

        return count