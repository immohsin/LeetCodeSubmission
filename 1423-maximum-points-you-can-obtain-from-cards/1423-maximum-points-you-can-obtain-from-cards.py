class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints)
        n = len(cardPoints)
        if n == k:
            return s
        i = 0
        window = n - k
        res = 0
        win_s  = 0
        for j in range(len(cardPoints)):
            win_s+=cardPoints[j]
            if j-i+1 == window:
                res = max(res, s-win_s)
                win_s-=cardPoints[i]
                i+=1
        return res
                