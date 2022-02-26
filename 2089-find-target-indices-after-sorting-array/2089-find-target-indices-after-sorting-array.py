def first(arr, start, end, target):
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            res = mid
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else: start = mid + 1
    return res

def last(arr, start, end, target):
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            res = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else: start = mid + 1
    return res
            
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start, end = 0, len(nums) - 1
        r1 = first(nums, start, end, target)
        r2 = last(nums, start, end, target)
        if r1 != -1 and r2 != -1:
            return list(range(r1, r2+1))
        return []