class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                cur = c[i]
                for j in range(groupSize):
                    c[i + j] -= cur
                    if c[i + j] < 0:
                        return False
        return True