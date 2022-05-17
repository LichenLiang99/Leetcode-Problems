class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 0
        children = {i:[] for i in range(len(parent))}
        for i in range(1,len(parent)):
            children[parent[i]].append(i)

        def trav(v, prev_c):
            nonlocal ans, children
            if prev_c == s[v]:
                trav(v,"")
                return 0
            else:
                maxl, smaxl = 0,0
                for i in children[v]:
                    x = trav(i,s[v])
                    if x >= maxl:
                        smaxl = maxl
                        maxl = x
                    elif x > smaxl:
                        smaxl = x
                ans = max(ans,1+maxl+smaxl)
                return 1+maxl
        
        trav(0,"")
        return ans