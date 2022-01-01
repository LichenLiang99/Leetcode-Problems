class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()
        
        for cpd in cpdomains:
            count, domain = cpd.split()
            count = int(count)
            counter[domain] += count
            
            for i in range(len(domain)):
                if domain[i] == '.':
                    counter[domain[i+1 : ]] += count
        
        res = []
        for k, v in counter.items():
            res.append(str(v) + ' ' + k)
        
        return res