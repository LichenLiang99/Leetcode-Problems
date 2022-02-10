class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        patternMap = {}
        wordsMap = {}
        
        for c, w in zip(pattern, words):
            if c in patternMap and patternMap[c] != w:
                return False
            if w in wordsMap and wordsMap[w] != c:
                return False
            
            patternMap[c] = w
            wordsMap[w] = c
        
        return True