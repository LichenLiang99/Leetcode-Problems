class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        #use queue for bfs search
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft() #use .pop() if using dfs(stack)
                
                directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
                
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
#         def dfs(i, j):
#             if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
#                 return
#             grid[i][j] = '#'
#             dfs(i+1, j)
#             dfs(i-1, j)
#             dfs(i, j+1)
#             dfs(i, j-1)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    #dfs(r, c)
                    islands += 1
        
        return islands