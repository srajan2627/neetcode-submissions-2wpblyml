class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        maxlen = 1
        prevsign = ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prevsign != ">":
                prevsign = ">"
                maxlen = max(maxlen,right - left + 1)
                right += 1
            
            elif arr[right - 1] < arr[right] and prevsign != "<":
                prevsign = "<"
                maxlen = max(maxlen,right - left + 1)
                right += 1
            
            else:
                if arr[right - 1] == arr[right]:
                    right += 1
                else:
                    right = right
                left = right - 1
                prevsign = ""
            
        return maxlen

