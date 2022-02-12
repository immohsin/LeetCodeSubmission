class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(str(i) for i in digits)) + 1
        res = []
        while n:
            res.append(n%10)
            n = n//10
        return reversed(res)