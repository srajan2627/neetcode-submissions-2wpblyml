class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        j = 0
        maxsize = 0
        for i in range(len(arr)-2):
            if arr[i] >= arr[i+1] or arr[i+1] >= arr[i+2]:
                maxsize = max(maxsize,i - j + 1)
                j += 1
        
        return maxsize
