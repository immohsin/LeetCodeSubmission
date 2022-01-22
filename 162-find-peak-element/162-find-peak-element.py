class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1
        if n == 1:
            return 0

        while start <= end:
            mid = start + (end - start) // 2
            if mid > 0 and mid < n-1:
                if nums[mid] > nums[mid-1] and  nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid-1]:
                    end = mid - 1
                elif nums[mid] < nums[mid+1]:
                    start = mid + 1
            elif mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    start = mid + 1
            elif mid == n-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    end = mid - 1
                