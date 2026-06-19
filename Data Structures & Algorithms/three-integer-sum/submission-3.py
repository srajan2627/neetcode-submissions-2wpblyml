class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([a,nums[left],nums[right]])
                    left += 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

        return ans
                
    