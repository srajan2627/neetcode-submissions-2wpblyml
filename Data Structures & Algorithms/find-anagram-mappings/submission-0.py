class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums2)

        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    ans[i] = j
        
        return ans