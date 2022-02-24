import sys

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = sum(customers[x] for x in range(len(customers)) if grumpy[x] != 1)
        i = 0
        t = 0
        res = -sys.maxsize
        for j in range(len(customers)):
            if grumpy[j] == 1:
                t+=customers[j]
            if j-i+1 == minutes:
                res = max(t+s, res)
                if grumpy[i] == 1:
                    t-=customers[i]
                i+=1
        return res