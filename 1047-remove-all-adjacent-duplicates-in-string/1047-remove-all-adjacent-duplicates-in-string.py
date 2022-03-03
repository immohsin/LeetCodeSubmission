class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = ""
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        for j in stack:
            ans+=j
        return ans