class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        r_b_c = 0
        c_b_c = 0
        
        for col in range(len(picture)):
            for row in range(len(picture)):

                if picture[col][row] == 'B':
                    r_b_c += 1
                    if r_b_c == 1:
                        count += 1
                        r_b_c = 0

                elif picture[row][col] == 'B':
                    c_b_c += 1
                    if c_b_c == 1:
                        count += 1
                        c_b_c = 0
        
        return count

