class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] & 1:
                nums[i] = 1
            else:
                nums[i] = 0

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        res = 0
        d = {0: 1}
        for i in range(n):
            freq = d.get(prefix[i] - k)
            if freq:
                res+=freq
            d[prefix[i]] = d.get(prefix[i], 0) + 1
        return res
                
                
                
            
                
            
                