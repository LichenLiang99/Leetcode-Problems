class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words = sorted(words, key = lambda x : len(x))
        for word in words:
            for i in range(len(word)):
                subword = word[:i] + word[i+1:]
                lens = dp.get(subword,0) + 1
                lenw = dp.get(word,0)
                dp[word] = max(lens, lenw)
        
        return max(dp.values())