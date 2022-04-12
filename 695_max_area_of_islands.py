class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col, maxarea = len(grid), len(grid[0]), 0
        def area(x, y):
            if (not(0<=x<row and 0<=y<col)) or (grid[x][y] == 0):
                return 0
			
            grid[x][y] = 0
            return 1 + area(x, y-1) + area(x-1, y) + area(x, y+1) + area(x+1, y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxarea = max(area(i, j), maxarea)

        return maxarea
        
