class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        
        q = collections.deque([])
        
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    height[r][c] = 0
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        while q:
            r, c = q.popleft()
            for x, y in directions:
                newr = r + x
                newc = c + y
                if newr < 0 or newr >= rows or newc < 0 or newc >= cols or height[newr][newc] != -1:
                    continue
                else:
                    height[newr][newc] = height[r][c] + 1
                    q.append((newr,newc))
        
        return height