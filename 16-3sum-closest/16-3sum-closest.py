class Solution:
    def threeSumClosest(self, arr: List[int], target_sum: int) -> int:
        arr.sort()

        result = sum(arr[:3])
        for i, n in enumerate(arr):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            l = i + 1
            r = len(arr) - 1

            while l < r:
                currSum = n + arr[l] + arr[r]
                if currSum == target_sum:
                    return currSum
                if abs(currSum - target_sum) <  abs(result - target_sum):
                    result = currSum
                if currSum > target_sum:
                    r -= 1
                else: 
                    l += 1

        return result