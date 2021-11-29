class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #store rightmost index of letter
        rightmost = {c:i for i, c in enumerate(s)}
        
        size, end = 0, 0

        res = []
        for i, c in enumerate(s):

            size += 1
            end = max(end, rightmost[c])
            if i == end:
                res.append(size)
                size = 0

        return res