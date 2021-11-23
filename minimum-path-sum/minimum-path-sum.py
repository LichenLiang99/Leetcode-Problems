class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        #bottom up dp
        #created extra row and col to the bottom and right
        res = [[float("inf")] * (col + 1) for _ in range(row + 1)]
        
        #change value in row below bottom right for math calculation
        res[row - 1][col] = 0
        
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        
        return res[0][0]
    
        
        