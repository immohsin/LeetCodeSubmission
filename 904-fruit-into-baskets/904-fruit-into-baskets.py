class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d,c = {}, 0
        i = 0
        f = 2
        res = 0
        for j in range(len(fruits)):
            d[fruits[j]] = d.get(fruits[j], 0) + 1
            if d[fruits[j]] == 1:
                c+=1
            if c > f:
                d[fruits[i]]-=1
                if d[fruits[i]] == 0:
                    c-=1
                i+=1
            if c <= f:
                res =max(res, j-i+1)
        return res
                