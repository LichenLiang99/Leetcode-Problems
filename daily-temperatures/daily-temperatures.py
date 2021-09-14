class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        rightMax = 0

        
        #start from the right of the list
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            
            #if rightMax temperature is less than our current temperature, update rightMax
            #meaning we are at hottest temp
            if rightMax <= t:
                rightMax = t
            #otherwise, there is future warmer temperature
            else:
                days = 1
                #as long as future temperature is less than our current temperature, days add up.
                #stops until hotter temperature is reached, and update res[]
                while temperatures[i+days] <= t:
                    days += res[i+days]
                res[i] = days
        
        return res
        
        #time o(n), space o(1) concept dp

        
        #-----------------Using Stack----------
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans
    #time o(n) space o(n)
    