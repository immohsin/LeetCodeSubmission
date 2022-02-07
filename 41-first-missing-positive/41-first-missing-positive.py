class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = 2**31 - 1
        for i in range(1, n+1):
            if i not in nums:
                return i