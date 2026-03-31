class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #k = k % len(nums)
        i = 0
        j = len(nums)
        while i < j - 1:
            nums[i],nums[j-1] = nums[j-1], nums[i]
            j -= 1
            i += 1

        i = 0
        n = k
        while i < n:
            nums[i], nums[n - 1] = nums[n - 1],nums[i]
            n -= 1
            i += 1

        i = k
        l = len(nums) - 1
        while i < l:
            nums[i],nums[l] = nums[l], nums[i]
            l -= 1
            i += 1
        