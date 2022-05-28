class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid) * len(grid[0])
        ans = 0
        
        med = sorted([col for row in grid for col in row])[n // 2]
        
        for row in grid:
            for col in row:
                if abs(med-col) % x != 0:
                    return -1
                ans+= abs(med-col) // x
        
        return ans
