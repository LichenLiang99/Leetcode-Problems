class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        bound = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        
        def dfs(i, j):
            grid[i][j] = -1
            for dr, dc in directions:
                newR = i + dr
                newC = j + dc
                
                if newR >= 0 and newC >= 0 and newR < rows and newC < cols:
                    if grid[newR][newC] == 0:
                        bound.add((i,j))
                    elif grid[newR][newC] == 1:
                        dfs(newR,newC)
        
        def getFirst():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return i,j
        
        i, j = getFirst()
        dfs(i,j)
        
        res = 0
        
        while bound:
            new = []
            for i, j in bound:
                for dr, dc in directions:
                    newR = i + dr
                    newC = j + dc
                    if newR >= 0 and newC >= 0 and newR < rows and newC < cols:
                        if grid[newR][newC] == 1:
                            return res
                        elif grid[newR][newC] == 0:
                            grid[newR][newC] = -1
                            new.append((newR, newC))
            res += 1
            bound = new