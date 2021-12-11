class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        rows = len(heightMap)
        cols = len(heightMap[0])
        heap = []
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i,j))
        
        res = 0
        
        while heap:
            
            height, i, j = heapq.heappop(heap)
            directions = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for x, y in directions:
                if x>=0 and x<rows and y>=0 and y<cols and (x,y) not in visited:
                    res += max(0, height - heightMap[x][y])
                    heapq.heappush(heap,(max(heightMap[x][y], height), x, y))
                    visited.add((x,y))
        return res