class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        #Initiate the counter to zero
        #Iterate over k from 1 to sqrt(2N+0.25) - 0.5
        #Decrese N by k to keep xk term only
        #verify if x is integer, if so increase counter



        count = 0
        upper_limit = ceil((2 * n + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            n -= k
            if n % k == 0:
                count += 1
        return count
    
    
        # count = 0
        # for i in range(1, int(math.sqrt(N))+1):
        #     if N%i == 0:
        #         if i%2:
        #             count += 1
        #         if (N/i)%2 and N/i != i:
        #             count += 1
        # return count