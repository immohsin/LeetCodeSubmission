class Solution:
    def makeGood(self, s: str) -> str:
        res = ""
        stack = []
        for i in range(len(s)):
            if stack and (chr(ord(stack[-1]) - 32) == s[i] or chr(ord(s[i]) - 32) == stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
        while stack:
            res+=stack.pop()
        return res[::-1]