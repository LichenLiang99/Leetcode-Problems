class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #bottom up dp
        #top down recursive
        row = len(matrix)
        col = len(matrix[0])
        mapp = {} #(r,c) -> maxlength of square
        
        def helper(r,c):
            if r >= row or c >= col:
                return 0
            
            if (r,c) not in mapp:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)
            
                mapp[(r,c)] = 0

                if matrix[r][c] == "1":
                    mapp[(r,c)] = 1 + min(down, right, diag)
            
            return mapp[(r,c)]
        
        helper(0,0)
        return max(mapp.values()) ** 2
    
    #time o(mn) space o(mn)