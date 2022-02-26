import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 0
        res = [0] * len(arr)
        prev = None
        heap = []
        for i, ele in enumerate(arr):
            heapq.heappush(heap, (ele, i))

        while heap:
            ele, idx = heapq.heappop(heap)
            if prev != ele:
                rank+=1
            prev = ele
            res[idx] = rank
        return res
        