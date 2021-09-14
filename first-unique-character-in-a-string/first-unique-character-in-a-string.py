class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = defaultdict(int)
        for i in s:
            ht[i] += 1
        for index, character in enumerate(s):
            if ht[character] == 1:
                return index
        return -1