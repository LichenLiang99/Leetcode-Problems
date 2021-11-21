class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN = 0
        closeN = 0
        
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            #done condition
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            #open must < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            #close must < open
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        
        backtrack(0, 0)
        return res