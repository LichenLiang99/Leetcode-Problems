class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        visited = set()
        res = []
        for i, j in adjacentPairs:
            adj[i].append(j)
            adj[j].append(i)
        
        endPt = [x for x in adj if len(adj[x]) == 1]
        
        def dfs(v):
            res.append(v)
            visited.add(v)
            for i in adj[v]:
                if i not in visited:
                    dfs(i)
            
        
        dfs(endPt[0])
        return res