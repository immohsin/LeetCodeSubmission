from collections import Counter
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans, ans_len = "", 0
        for i in range(len(s)):
            for j in range(len(s)):
                if j-i+1 >= 2:
                    if isNice(s[i:j+1]):
                        if j-i+1 > ans_len:
                            ans = s[i:j+1]
                            ans_len = j-i+1
        return ans

    
def isNice(substr):
    count_map = Counter(substr)
    for char in count_map.keys():
        if char.isupper():
            if not char.lower() in count_map:
                return False
        else:
            if not char.upper() in count_map:
                return False
    return True
