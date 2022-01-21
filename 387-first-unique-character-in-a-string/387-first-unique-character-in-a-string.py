class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = [0 for _ in range(26)]
        for i in s:
            charMap[ord(i) - ord('a')]+=1
        
        for i in range(len(s)):
            if charMap[ord(s[i]) - ord('a')] == 1:
                return i
        return -1
        