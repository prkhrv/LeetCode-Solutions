class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return image
        
        row, col = len(image), len(image[0])
        old_col = image[sr][sc]
        
        def dfs(r,c):
            if not (0 <= r < row and 0 <= c < col) or image[r][c] != old_col or image[r][c] == newColor:
                return
            
            image[r][c] = newColor
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
