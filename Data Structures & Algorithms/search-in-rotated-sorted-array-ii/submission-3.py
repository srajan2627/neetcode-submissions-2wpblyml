class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True 
  
            # 1. The Emergency Escape (Handles tricky duplicates)
            if nums[left] == nums[mid] == nums[right]:
                right -= 1

            # 2. Left half is perfectly sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 3. Right half is perfectly sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return False