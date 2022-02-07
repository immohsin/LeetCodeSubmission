class Solution:
    def minimumSum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        i, j = 0, len(s) - 1
        num1 = int(s[i] + s[j])
        num2 = int(s[i+1] + s[j-1])
        return num1 + num2
            