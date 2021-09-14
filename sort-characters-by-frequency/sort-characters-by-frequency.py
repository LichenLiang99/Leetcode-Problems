class Solution:
    def frequencySort(self, s: str) -> str:
        
        max_freq = 0
        counts = defaultdict(int)
        string = list(s)
        for s in string:
            counts[s] += 1
        for i in counts:
            max_freq = max(max_freq, counts[i])
            
        #to rewrite above code
        #counts = collections.Counter(s)
        #max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)
        
        #time o(n), space o(n), concept hashmap, bucket sort
        