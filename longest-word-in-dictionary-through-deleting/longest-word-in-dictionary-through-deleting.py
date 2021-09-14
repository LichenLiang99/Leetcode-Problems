class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        dictionary.sort(key = lambda x : (-len(x), x))
        
        def helper(word, string):
            w = len(word)
            s = len(string)
            pw, ps = 0, 0
            
            while ps < s and pw < w:
                if word[pw] == string[ps]:
                    pw += 1
                ps += 1
            
            return pw == w
            
        for word in dictionary:
            if helper(word, s):
                return word
        
        return ""