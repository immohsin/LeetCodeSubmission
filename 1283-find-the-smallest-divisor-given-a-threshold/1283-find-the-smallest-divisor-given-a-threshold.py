import math

def get_result(nums, divisor, k):
    s = 0
    for i in nums:
        s+=(math.ceil(i/divisor))
        if s > k:
            return False
    return True


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        while start <= end:
            divisor = start + (end - start) // 2
            if get_result(nums, divisor, threshold):
                end = divisor - 1
            else:
                start = divisor + 1
        return start