class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        num_occ = defaultdict(int)
        ans_arr = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                num_occ[mat[i][j]] += 1

        for k,v in num_occ.items():
            if v == len(mat):
                ans_arr.append(k)
        
        if ans_arr:
            return min(ans_arr)
        else:
            return -1
        