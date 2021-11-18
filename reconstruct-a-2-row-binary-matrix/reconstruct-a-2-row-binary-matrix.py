class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        upperlist = [0 for _ in range(len(colsum))]
        lowerlist = [0 for _ in range(len(colsum))]
        
        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper > lower:
                    upperlist[i] = 1
                    upper -= 1
                else:
                    lowerlist[i] = 1
                    lower -= 1
            elif colsum[i] == 2:
                upperlist[i] = 1
                lowerlist[i] = 1
                upper -= 1
                lower -= 1
                
        if upper == 0 and lower == 0:
            return [upperlist,lowerlist]
        else:
            return []