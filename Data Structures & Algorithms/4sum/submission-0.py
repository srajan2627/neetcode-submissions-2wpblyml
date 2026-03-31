class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                b = nums[j]
                if j > i+1 and b == nums[j-1]:
                    continue

                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum_of_four = a + b + nums[l] + nums[r]
                    if sum_of_four > target:
                        r -= 1
                    elif sum_of_four < target:
                        l += 1
                    else:
                        ans.append([a,b,nums[l],nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        
        return ans
