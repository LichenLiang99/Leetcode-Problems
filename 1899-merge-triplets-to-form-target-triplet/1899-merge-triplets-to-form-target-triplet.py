class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goodIndex = set() 
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for idx, val in enumerate(triplet):
                if val == target[idx]:
                    goodIndex.add(idx)
            
        return len(goodIndex) == 3