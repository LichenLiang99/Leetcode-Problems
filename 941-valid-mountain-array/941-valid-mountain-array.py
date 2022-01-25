class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == len(arr) - 1:
            return False
        
        while i+1 < n and arr[i+1] < arr[i]:
            i += 1
        
        return i == len(arr) - 1