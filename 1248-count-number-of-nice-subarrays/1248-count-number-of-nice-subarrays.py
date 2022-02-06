class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] & 1:
                nums[i] = 1
            else:
                nums[i] = 0

        res = 0
        d = {0: 1}
        s = 0
        for i in range(n):
            s+= nums[i]
            freq = d.get(s - k)
            if freq:
                res+=freq
            d[s] = d.get(s, 0) + 1
        return res
                
                
                
            
                
            
                