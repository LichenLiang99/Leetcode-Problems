class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #store parent of each node, initially parent is itself
        parent = [i for i in range(len(edges) + 1)]
        
        #store rank of each node, initially 1
        rank = [1] * (len(edges) + 1)
        
        #find uppermost parent
        def findparent(n):
            p = parent[n]
            
            #while parent of p is not itself
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            
            return p
        
        #join the 2 nodes if possible
        def union(n1, n2):
            p1 = findparent(n1)
            p2 = findparent(n2)
            
            #if they have same parent, then adding edge in between would result in cycle
            #so return this edge
            if p1 == p2:
                return False
            
            #node with smaller rank is added to the larger rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        #if 2 nodes can't merge(have same parent), they must for a cycle
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
        
        #time o(n) space o(n)