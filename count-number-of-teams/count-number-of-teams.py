class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #for each value in list:
        #count left less than * right greater than and multiply to get ascending counter
        #count left greater than * right less than and multiply to get descending counter
        ascendingCounter = descendingCounter = 0
        
        for index, val in enumerate(rating):
            leftless = leftgreater = rightless = rightgreater = 0
            
            #record left portion and increment counter accordingly
            for n in rating[0:index]:
                if n < val:
                    leftless += 1
                elif n > val:
                    leftgreater += 1
            
            #record right portion and increment counter accordingly
            for n in rating[index+1:]:
                if n < val:
                    rightless += 1
                elif n > val:
                    rightgreater += 1
                    
            ascendingCounter += leftless * rightgreater
            descendingCounter += leftgreater * rightless
            
        return ascendingCounter + descendingCounter