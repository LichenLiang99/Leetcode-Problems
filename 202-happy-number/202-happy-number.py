class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        
        def findSumSquare(n):
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10

            return output
    
        while True:
            slow = findSumSquare(slow)
            fast = findSumSquare(findSumSquare(fast))
            
            if slow == fast:
                break
        
        return slow == 1
    
        
    