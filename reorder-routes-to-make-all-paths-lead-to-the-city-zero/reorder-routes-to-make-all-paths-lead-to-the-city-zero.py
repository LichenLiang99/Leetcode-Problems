class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        neighbors = {city : [] for city in range(n)}
        visited = set()
        counter = 0
        
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbors, visited, counter
            
            
            for n in neighbors[city]:
                if n in visited:
                    continue
                
                if (n, city) not in edges:
                    counter += 1
                
                visited.add(n)
                dfs(n)
            
        visited.add(0)
        dfs(0)
        return counter
    
    #time o(n) space o(n)