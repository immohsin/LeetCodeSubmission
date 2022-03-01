class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n -1
        if n == 1:
            return nums[0]
        if nums[start] < nums[end]:
            return nums[0]
        while start <= end:
            mid = start + ((end - start) // 2)
            nxt = (mid + 1) % n
            prev = (mid -1 + n) % n
            if nums[mid] < nums[prev] and nums[mid] <= nums[nxt]:
                return nums[mid]
            elif nums[start] == nums[end]:
                end-=1
            elif nums[mid] >= nums[0]:
                start = mid + 1
            elif nums[mid] <= nums[-1]:
                end = mid - 1
        return nums[0]