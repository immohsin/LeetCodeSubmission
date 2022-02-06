class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        d = {0: 1}
        for j in range(len(nums)):
            s+=nums[j]
            freq = d.get(s-k)
            if freq:
                res+=freq
            d[s] = d.get(s, 0) + 1
        return res
            
        