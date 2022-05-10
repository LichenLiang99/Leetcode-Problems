class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using bubble sort
        #count has max size of n, freq has max size of count which is also n (every element appears only once)
        #time o(n) space o(n) concept: bubblesort, hashmap, array
        
        #hashmap to store how many times each value occured
        #and an array that index is count of occurence and value is list of numbers with that frequency
        #count = collections.Counter(nums) #1
        count = defaultdict(int) #2
        freq = [[] for i in range(len(nums) + 1)]
        
        #hashmap to count frequencies #2 method
        for n in nums:
            count[n] += 1 
        #for each number, count pair, use count as key and add n to list
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        #start from highest frequency and move downwards
        for i in range(len(freq) - 1, 0, -1):
            #at freq[count], there can be more than one numbers in the list
            for n in freq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
                
        #------------------
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        #Space O(N+k)
        return heapq.nlargest(k, count.keys(), key=count.get) 
       
        
        