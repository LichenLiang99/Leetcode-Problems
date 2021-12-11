class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows-1, cols-1)
        
        if k >= rows - 1 + cols - 1:
            return rows - 1 + cols - 1
        
        state = (0,0,k)
        q = collections.deque([(0, state)])
        visited = set([state])
        
        
        while q:
            steps, (r, c, k) = q.popleft()
            
            if (r,c) == target:
                return steps
            
            directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for newrow, newcol in directions:
                if newrow >= 0 and newrow < rows and newcol >=0 and newcol < cols:
                    new_elimination = k - grid[newrow][newcol]
                    new_state = (newrow, newcol, new_elimination)
                    if new_elimination >= 0 and new_state not in visited:
                        q.append((steps + 1, new_state))
                        visited.add(new_state)
        
        return -1