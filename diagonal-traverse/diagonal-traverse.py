class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mapp = {} #　i+j : []
        res = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in mapp:
                    mapp[i+j] = [mat[i][j]]
                else:
                    mapp[i+j].append(mat[i][j])
        
        for i in mapp.items():
            
            #if sum of index is divisible by 2
            #append in reverse order
            #i is (key:value)
            #i (2:[3,5,7]) append in order 7 5 3
            if i[0] % 2 == 0:
                [res.append(x) for x in i[1][::-1]]
            else:
                [res.append(x) for x in i[1]]
        
        return res
        
        #time o(n) space o(n)