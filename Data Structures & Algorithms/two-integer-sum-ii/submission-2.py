class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        for right in range(1,len(numbers)):
            if numbers[right] + numbers[left] == target:
                return [numbers[left],numbers[right]]
            else:
                left += 1
            