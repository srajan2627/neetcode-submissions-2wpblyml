class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] != nums2[j]:
                    continue
                elif nums1[i] == nums2[j]:
                    if j == len(nums2) -1 or nums2[j+1] < nums1[i]:
                        ans[i] = -1
                    else:
                        ans[i] = nums2[j+1]
        
        return ans