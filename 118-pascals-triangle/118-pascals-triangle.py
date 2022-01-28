class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            prevRow = [0] + res[-1] + [0]
            currRow = []
            for j in range(len(res[-1])+1):
                currRow.append(prevRow[j] + prevRow[j + 1])
            
            res.append(currRow)
        
        return res
                