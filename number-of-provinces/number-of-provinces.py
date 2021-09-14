class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(pair):
            for i, j in enumerate(isConnected[pair]):
                if j and i not in visited:
                    visited.add(i)
                    dfs(i)
        
        
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces