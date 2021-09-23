class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r-l):
                top = l
                bot = r
                topleft = matrix[top][l+i]
                
                #bot left to top left
                matrix[top][l+i] = matrix[bot-i][l]
                
                #bot right to bot left
                matrix[bot-i][l] = matrix[bot][r-i]
                
                #top right to bot right
                matrix[bot][r-i] = matrix[top+i][r]
                
                #top left to top right
                matrix[top+i][r] = topleft
                
            l += 1
            r -= 1