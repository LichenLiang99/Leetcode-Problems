class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def backtrack(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i,a) in dp:
                return dp[(i,a)]
            
            dp[(i,a)] = backtrack(i, a + coins[i]) + backtrack(i+1, a)
            
            return dp[(i,a)]
        
        return backtrack(0, 0)