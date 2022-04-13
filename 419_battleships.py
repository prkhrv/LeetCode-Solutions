class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        if len(board) == 0:
            return 0
        
        if len(board[0]) == 0:
            return 0        
        
        m, n = len(board), len(board[0])
        
        res = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                if board[i][j] == 'X':
                    res += 1
        
        return res
