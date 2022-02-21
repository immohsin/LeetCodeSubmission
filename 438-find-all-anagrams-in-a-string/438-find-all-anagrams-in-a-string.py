from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        res = []
        d = Counter(p)
        c = len(d)
        k = len(p)
        for j in range(len(s)):
            if d.get(s[j]) != None:
                d[s[j]]-=1
                if d[s[j]] == 0:
                    c-=1
            if (j-i+1) == k:
                if c == 0:
                    res.append(i)
                if d.get(s[i]) != None:
                    d[s[i]]+=1
                    if d[s[i]] == 1:
                        c+=1
                i+=1
        return res
                    
            