class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1):
        res = n1
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True
        
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        
        for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            visited = set()
            for x, y, _ in group:
                visited.add(x)
                visited.add(y)
                uf.union(x,y)
            for x in visited:
                if uf.find(x) != uf.find(0):
                    uf.parent[x] = x
        return [x for x in range(n) if uf.find(x) == uf.find(0)]
                
        