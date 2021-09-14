class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        dp = [False] * (len(s) + 1)
        
        #base case, location after last value is true
        dp[len(s)] = True
        
        #work backwords starting from last index
        for i in range(len(s) - 1, -1, -1):
            
            #for each word in dictionary
            for w in wordDict:
                
                #sum of current position and word length should be less than our string
                #AND if substring match the word
                #then set dp[i] to true
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)] #i.e since dp[8] is true, then dp[4] is also true
                    
                #move on to next i
                if dp[i]:
                    break
        
        #first value must be true to match
        return dp[0]