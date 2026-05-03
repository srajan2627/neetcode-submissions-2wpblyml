class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        largest = 0
        ans = 0

        while r < len(nums) - 1:
            for i in range(l,r+1):
                largest = max(largest,i + nums[i])
            ans += 1
        
        return ans