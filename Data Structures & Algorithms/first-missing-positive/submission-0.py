class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. First Pass: Put each number in its "correct seat"
        for i in range(n):
            # Keep swapping until the current number is in its correct seat,
            # or it's out of bounds (<= 0 or > n), or it's a duplicate.
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Figure out where this number actually belongs
                correct_idx = nums[i] - 1
                
                # Swap it into its correct seat
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # 2. Second Pass: Look for the first broken chair
        for i in range(n):
            # If index 0 doesn't have 1, then 1 is missing!
            if nums[i] != i + 1:
                return i + 1
                
        # 3. If everything is perfectly in its place, the missing number is n + 1
        return n + 1