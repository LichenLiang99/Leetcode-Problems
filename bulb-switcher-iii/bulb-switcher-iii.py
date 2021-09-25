class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        rightmost = 0
        counter = 0
        for i, a in enumerate(light, 1):
            rightmost = max(rightmost, a)
            if rightmost == i:
                counter += 1
        return counter