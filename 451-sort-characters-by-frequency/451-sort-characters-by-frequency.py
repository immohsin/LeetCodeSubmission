import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        n = 0
        res = ""
        d = Counter(s)
        for k, v in d.items():
            heapq.heappush(heap, (-v, k))
            n+=1
        while n:
            val, char = heapq.heappop(heap)
            res+=(char * -val)
            n-=1
        return res
            