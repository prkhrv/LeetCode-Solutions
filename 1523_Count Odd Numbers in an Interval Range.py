class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 !=0 or high % 2 !=0:
            ans = 1
        else:
            ans = 0
        
        ans += (high - low) // 2
        
        return ans
        
