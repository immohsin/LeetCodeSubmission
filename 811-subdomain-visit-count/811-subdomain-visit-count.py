class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}

        for pair in cpdomains:
            countpair = pair.split(" ")
            rep = int(countpair[0])
            domain = countpair[1].split(".")
            for i in range(len(domain)):
                sub = '.'.join(domain[i:])
                domains.setdefault(sub, []).append(rep)

        return [f'{sum(j)} {i}' for i, j in domains.items()]