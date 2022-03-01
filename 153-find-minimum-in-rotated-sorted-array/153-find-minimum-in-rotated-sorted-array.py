class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            prev = (mid - 1 + n) % n
            nxt = (mid + 1) % n
            if nums[prev] > nums[mid] < nums[prev]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                start = mid + 1
            elif nums[mid] <= nums[-1]:
                end = mid
        return nums[0]