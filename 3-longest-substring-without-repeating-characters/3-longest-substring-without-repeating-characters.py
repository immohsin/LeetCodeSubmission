class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        d = {}
        res = 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            while d[s[j]] > 1:
                d[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res