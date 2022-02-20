from collections import Counter
import sys

def is_present(d, c):
    return False if d.get(c) == None else True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        k = Counter(t)
        c = len(k)
        i = 0
        l = 0
        r = 0
        res = sys.maxsize
        for j in range(len(s)):
            if is_present(k, s[j]):
                k[s[j]]-=1
                if k[s[j]] == 0:
                    c-=1
            while c == 0:
                if (j-i+1) < res:
                    res = j-i+1
                    l = i
                    r = j+1
                if is_present(k, s[i]):
                    k[s[i]]+=1
                    if k[s[i]] == 1:
                        c+=1
                i+=1
        return s[l:r]
            
            
            