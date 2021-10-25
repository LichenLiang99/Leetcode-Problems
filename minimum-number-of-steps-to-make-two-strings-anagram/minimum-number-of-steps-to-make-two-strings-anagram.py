class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mapp = collections.Counter(s)
        res = 0
        for i in t:
            if mapp[i] > 0:
                mapp[i] -= 1
            else:
                res += 1
        return res