class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        
        i = 0
        left = m
        while i < len(nums2):
            nums1[left] = nums2[i]
            i += 1
            left += 1
        
        nums1.sort()