class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        s = []
        for i in num:
            while s and i < s[-1] and k:
                s.pop()
                k-=1
            s.append(i)
        # print(s)
        while k > 0:
            s.pop()
            k-=1
        while len(s) > 1 and s[0] == '0':
            s.pop(0)
        return "".join(s)
                