class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        d = {}
        for cpdomain in cpdomains:
            split_1 = cpdomain.split(" ")
            rep = int(split_1[0])
            new = split_1[1].split('.')
            for j in range(len(new)-1,-1,-1):
                s = ".".join(new[j:])
                d[s] = d.get(s, 0) + rep
        res = [str(v) + " " + k for k,v in d.items()]
        return res