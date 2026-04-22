class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        O_X = 0
        O_Y = 0
        dist_val_list = []
        ans = []
        for i in range(len(points)):
            X = points[i][0]
            Y = points[i][1]
            sq_X = (X - O_X)**2
            sq_Y = (Y - O_Y)**2
            EQ_dist = sq_X + sq_Y

            dist_val = math.sqrt(EQ_dist)
            dist_val_list.append((dist_val,[X,Y]))

        sort_list = sorted(dist_val_list, key=lambda item: item[0])
        ans = []
        for i in range(k):
            ans.append(sort_list[i][1])
        return ans

        
        





