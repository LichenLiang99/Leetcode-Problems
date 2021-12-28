class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        freq = {}
        
        for r in range(len(fruits)):
            right = fruits[r]
            if right not in freq:
                freq[right] = 0
            freq[right] += 1
            
            while len(freq) > 2:
                left = fruits[l]
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]
                    
                l += 1
            
            res = max(res, r - l + 1)
        
        return res