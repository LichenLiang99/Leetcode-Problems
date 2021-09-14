class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        #old row*col must equal to new row*col
        if m * n != r * c:
            return mat
        
        #add all elements to 1D array
        oneRow = []
        for i in mat:
            for j in i:
                oneRow.append(j)
        
        #add row by row to the matrix with c columns
        res = []
        for i in range(0, len(oneRow), c):
            res.append(oneRow[i : i+c])
        
        return res
    
    #time o(n*m) space o(n*m) concept matrix, array