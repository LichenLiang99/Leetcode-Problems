class Solution:
    def decodeString(self, string: str) -> str:
        s = []
        
        for i in range(len(string)):
            if string[i] != "]":
                s.append(string[i])
            else:
                sub = ""
                while s[-1] != "[":
                    sub = s.pop() + sub
                s.pop() #pop [
                
                k = ""
                while s and s[-1].isdigit():
                    k = s.pop() + k
                
                s.append(int(k) * sub)
        
        return "".join(s)
                