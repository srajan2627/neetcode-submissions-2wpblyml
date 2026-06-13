class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        # Helper function to check if a target 'max_sum' is valid
        def canSplit(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                # If adding the next number exceeds our guessed max_sum...
                if current_sum + num > max_sum:
                    # ...we are forced to start a brand new subarray
                    subarrays += 1
                    current_sum = num
                    
                    # If we need more than k subarrays, this max_sum is impossible
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            
            return True

        # 1. Establish the search boundaries for the ANSWER
        left = max(nums)
        right = sum(nums)
        
        # 2. Binary Search on the answer range
        while left < right:
            mid = (left + right) // 2
            
            # If it's possible to split the array with 'mid' as the max sum
            if canSplit(mid):
                # Try to look for an even smaller, tighter maximum sum
                right = mid
            else:
                # 'mid' was too small, we need a larger allowance for our sum
                left = mid + 1
                
        return left