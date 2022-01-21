import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        d = Counter(s)
        heap = [(-v, k) for k, v in d.items()]
        heapq.heapify(heap)
        while heap:
            val, char = heapq.heappop(heap)
            res.append(char * -val)
        return "".join(res)
            