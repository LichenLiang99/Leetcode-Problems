class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #original | new | state
        #     0      0      0
        #     1      0      1
        #     0      1      2
        #     1      1      3
        
        rows = len(board)
        cols = len(board[0])
        
        def countNeighbor(currR, currC):
            neighborCount = 0
            for i in range(currR-1, currR+2):
                for j in range(currC-1, currC+2):
                    if ((i == currR and j == currC) or i < 0 or j < 0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        neighborCount += 1
            return neighborCount
        
        
        for r in range(rows):
            for c in range(cols):
                neighbors = countNeighbor(r,c)
                
                if board[r][c]:
                    if neighbors in [2, 3]:
                        board[r][c] = 3      
                elif neighbors == 3:
                    board[r][c] = 2

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1