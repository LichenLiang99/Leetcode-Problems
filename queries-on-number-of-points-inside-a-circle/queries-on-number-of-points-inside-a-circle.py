class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for idx, q in enumerate(queries):
            x, y, r = q
            r2 = r * r
            for i, j in points:
                if (x-i)**2 + (y-j)**2 <= r2:
                    res[idx] += 1
        return res