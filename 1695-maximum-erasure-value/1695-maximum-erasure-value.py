class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        d = {}
        s, res = 0,0
        for j in range(len(nums)):
            d[nums[j]] = d.get(nums[j], 0) + 1
            s+=nums[j]
            while d[nums[j]] > 1:
                d[nums[i]]-=1
                s-=nums[i]
                i+=1
            res = max(res, s)
        return res