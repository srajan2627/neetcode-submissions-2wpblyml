class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] != nums2[j]:
                    continue
                elif nums1[i] == nums2[j]:
                    ans[i] = -1
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            ans[i] = nums2[k]
                            break
        
        return ans