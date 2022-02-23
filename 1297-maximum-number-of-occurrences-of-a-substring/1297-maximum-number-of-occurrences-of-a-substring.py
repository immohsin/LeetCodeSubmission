from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = {}
        i = 0
        res = 0
        sstr = []
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            while len(d) > maxLetters:
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
            while maxSize < sum(d.values()) < minSize:            
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
            while len(d) <= maxLetters and maxSize >= sum(d.values()) >= minSize:
                sstr.append(s[i:j+1])
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
                
        c = Counter(sstr)
        return max(c.values()) if len(c) else 0