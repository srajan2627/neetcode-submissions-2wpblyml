class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            max_ele = 0
            if i == n - 1:
                arr[i] = - 1
                break
            for j in range(i+1,n):
                max_ele = max(max_ele,arr[j])
            arr[i] = max_ele

        return arr