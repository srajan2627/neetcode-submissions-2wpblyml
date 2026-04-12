class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            sq = (l + r)//2
            if sq**2 == x:
                return sq
            elif sq**2 > x:
                r = sq - 1
            else:
                l = sq + 1
        
        return r