class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        d, c = {}, 0
        i = 0
        res = 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            if (j-i+1) == 3:
                if sum(d.values()) == 3 and len(d) == 3:
                    res+=1
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
        return res