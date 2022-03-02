class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        start, end = 1, position[-1] - position[0]
        while start <= end:
            diff = start + (end - start) // 2
            if canPlace(position, m , diff):
                start = diff + 1
            else:
                end = diff - 1
        return end
    

def canPlace(arr, balls, k):
    placed = 1
    prev = arr[0]
    for i in range(len(arr)):
        if (arr[i] - prev) >= k:
            placed+=1
            prev = arr[i]
        if placed == balls:
            return True
    return False