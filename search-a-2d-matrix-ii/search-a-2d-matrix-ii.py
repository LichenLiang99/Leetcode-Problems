class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        
        
        if row == 0 or col == 0 or target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False
        
        
        #start from bottom left
        r = row - 1
        c = 0
        
        
        while r >= 0 and c < col:
            if matrix[r][c] == target:
                return True
            
            #move up rows until target >= curr
            elif matrix[r][c] > target:
                r -= 1
            #move to the right until target <= curr
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
            
        
        return False
    
    