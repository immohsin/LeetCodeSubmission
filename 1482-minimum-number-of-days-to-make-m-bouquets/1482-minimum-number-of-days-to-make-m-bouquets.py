
def can_collect(day, bloomDay, k, m):
    i = 0
    bouket = 0
    while i < len(bloomDay):
        bloomed = True
        for j in range(i, i+k):
            if j >= len(bloomDay):
                return False
            if bloomDay[j] > day:
                bloomed = False
                break
        if bloomed:
            bouket+=1
        if bouket >= m:
            return True
        i = j+1
    return False

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return - 1
        res = -1
        maxDay = max(bloomDay)
        minDay = min(bloomDay)
        while minDay <= maxDay:
            mid = minDay + (maxDay - minDay) // 2
            if can_collect(mid, bloomDay, k, m):
                res = mid
                maxDay = mid - 1
            else:
                minDay = mid + 1
        return res