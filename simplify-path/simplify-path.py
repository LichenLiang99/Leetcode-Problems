class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for element in path.split('/'):
            if stack and element == '..':
                stack.pop()
            elif element not in ['..','.', '']:
                stack.append(element)
        
        return '/' + '/'.join(stack)