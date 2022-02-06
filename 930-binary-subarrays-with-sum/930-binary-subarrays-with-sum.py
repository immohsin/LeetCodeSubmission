class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        res = 0
        d = {0:1}
        for i in range(len(nums)):
            s+=nums[i]
            freq = d.get(s-goal)
            if freq:
                res+= freq
            d[s] = d.get(s, 0) + 1
        return res