class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                b = nums[j]

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    FourSum = a + b + nums[left] + nums[right]

                    if FourSum > target:
                        right -= 1

                    elif FourSum < target:
                        left += 1
                    else:
                        ans.append([a,b,nums[left],nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return ans