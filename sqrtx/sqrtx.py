class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 0, x // 2
        while l <= r:
            mid = l + (r-l) // 2
            num = mid * mid
            if num > x:
                r = mid - 1
            else:
                l = mid + 1

            
        return l - 1
    
    #time o(logn) space o(1) concept binary search