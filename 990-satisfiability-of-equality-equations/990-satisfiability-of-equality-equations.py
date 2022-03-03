class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        mapp = collections.defaultdict(set)
        noteq = []
        
        def canMeet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in mapp[u]:
                if v in visited:
                    continue
                if canMeet(v, target, visited):
                    return True
            return False
        
        for eq in equations:
            if eq[1:3] == '!=':
                noteq.append((eq[0], eq[3]))
            else:
                mapp[eq[0]].add(eq[3])
                mapp[eq[3]].add(eq[0])
        
        for u, v in noteq:
            if canMeet(u, v, set()):
                return False
        
        return True
    
        