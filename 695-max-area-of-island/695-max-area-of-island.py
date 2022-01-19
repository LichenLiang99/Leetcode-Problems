class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def bfs(i,j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))
            islandSize = 1
            while q:
                
                r, c = q.popleft()
                
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                
                for dr, dc in directions:
                    newR = dr + r
                    newC = dc + c
                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == 1 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append((newR, newC))
                        islandSize += 1
                        
            return islandSize 
        
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = bfs(r,c)
                    res = max(res, area)
        
        return res