def first(arr, start, end, t):
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == t:
            res = mid
            end = mid - 1
        elif arr[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    return res

def last(arr, start, end, t):
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == t:
            res = mid
            start = mid + 1
        elif arr[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    return res

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        start, end = 0, len(nums) - 1
        return [first(nums, start, end, target), last(nums, start, end, target)]