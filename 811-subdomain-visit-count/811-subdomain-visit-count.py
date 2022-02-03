class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        d = {}
        for cpdomain in cpdomains:
            rep = ""
            i = 0
            n = len(cpdomain)
            while i < n:
                if cpdomain[i] >= '0' and cpdomain[i] <= '9':
                    rep+=cpdomain[i]
                else:
                    break
                i+=1
            new = cpdomain[i+1:].split('.')
            for j in range(len(new)-1,-1,-1):
                s = ".".join(new[j:])
                d[s] = d.get(s, 0) + int(rep)

        for k,v in d.items():
            s = str(v) + " " + k
            res.append(s)
        return res