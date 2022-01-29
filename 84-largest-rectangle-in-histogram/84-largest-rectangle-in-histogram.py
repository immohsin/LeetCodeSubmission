class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            while len(s) and heights[i] < heights[s[-1]]:
                idx = s.pop()
                rMin = i
                lMin = s[-1] if len(s) else -1
                res = max(res, (rMin-lMin-1)*heights[idx])
            s.append(i)
        return res