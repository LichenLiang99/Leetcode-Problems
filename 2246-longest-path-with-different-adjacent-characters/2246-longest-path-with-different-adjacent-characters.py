class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        result = 0
        children = defaultdict(list)
        for i in range(1,len(parent)):
            children[parent[i]].append(i)

        def dfs(v, prev_child):
            nonlocal result, children
            if prev_child == s[v]:
                dfs(v,"")
                return 0
            else:
                maxl, smaxl = 0,0
                for i in children[v]:
                    x = dfs(i,s[v])
                    if x >= maxl:
                        smaxl = maxl
                        maxl = x
                    elif x > smaxl:
                        smaxl = x
                result = max(result,1+maxl+smaxl)
                return 1+maxl
        
        dfs(0,"")
        return result