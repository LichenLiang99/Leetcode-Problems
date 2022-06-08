class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.preSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.preSum[r][c+1]
                self.preSum[r+1][c+1] = prefix + above
        
        print(self.preSum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1
        
        bottomRight = self.preSum[r2][c2]
        above = self.preSum[r1 - 1][c2]
        left = self.preSum[r2][c1 - 1]
        topLeft = self.preSum[r1-1][c1-1]
        
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)