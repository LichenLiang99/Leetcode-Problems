class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))

            dictt[sorted_word].append(word)
            
        res = []
        for key in dictt:
            res.append(dictt[key])
        return res
            
