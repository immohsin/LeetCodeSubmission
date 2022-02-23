class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        d = {}
        i = 0
        res = []
        for j in range(len(s)):
            if j-i+1 == k:
                d[s[i:j+1]] = d.get(s[i:j+1], 0) + 1
                i+=1
        for k,v in d.items():
            if v > 1:
                res.append(k)
        return res