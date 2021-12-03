class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 1:
            for i in range(0,x+1):
                sq = i*i
                if sq == x:
                    return i
                elif sq > x:
                    return i-1
                elif sq < x:
                    continue
        else:
            return x
        
