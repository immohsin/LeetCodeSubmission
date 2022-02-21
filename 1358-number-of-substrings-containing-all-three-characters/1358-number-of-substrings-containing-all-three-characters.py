class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        d = {'a':0, 'b':0, 'c':0}
        res = 0
        for j in range(len(s)):
            d[s[j]]+=1
            while all(d.values()):
                res+=len(s) - j
                d[s[i]]-=1
                i+=1
        return res
                
                
                    