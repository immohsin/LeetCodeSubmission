class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                idx = s.pop()
                LMin = s[-1] if s else -1
                RMin = i
                idx_range = RMin - LMin - 1
                res = max(res, (idx_range*heights[idx]))
            s.append(i)
        return res
                