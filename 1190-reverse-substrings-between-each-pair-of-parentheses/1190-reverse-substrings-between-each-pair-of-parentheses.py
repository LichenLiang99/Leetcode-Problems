class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                temp = stack.pop()
                stack[-1] += temp[::-1]
            else:
                stack[-1] += c
        
        return stack[0]