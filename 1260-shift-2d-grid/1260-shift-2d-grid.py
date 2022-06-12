class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        def posToVal(r,c):
            return r * cols + c
        
        def valToPos(v):
            return [v // cols, v % cols]
        
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                newVal = (posToVal(r, c) + k) % (rows * cols)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
        
        return res