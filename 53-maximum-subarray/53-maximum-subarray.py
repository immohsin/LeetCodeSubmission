class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        if res < 0:
            return res
        cur_sum = 0
        for num in nums:
            cur_sum+=num
            cur_sum = max(cur_sum, num)
            res = max(cur_sum, res)
        return res