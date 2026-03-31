class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        min_boats = 0
        right = len(people) - 1

        while left <= right:
            rem_weight = limit - people[right]
            right -= 1
            min_boats += 1

            if left <= right and rem_weight >= people[left]:  
                left += 1
        
        return min_boats