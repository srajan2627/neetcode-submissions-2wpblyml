class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) 
        ans = [0] * n
        curr_max = -1
        for i in range(len(arr) - 1, -1,-1):
            ans[i] = curr_max
            curr_max = max(curr_max,arr[i])
        return ans
