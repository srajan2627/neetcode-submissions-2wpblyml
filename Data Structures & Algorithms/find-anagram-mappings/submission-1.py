class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums2)
        num_dict = {}

        for i in range(len(nums2)):
            num_dict[nums2[i]] = i

        for i in range(len(ans)):
            ans[i] = num_dict[nums1[i]]
        
        return ans
