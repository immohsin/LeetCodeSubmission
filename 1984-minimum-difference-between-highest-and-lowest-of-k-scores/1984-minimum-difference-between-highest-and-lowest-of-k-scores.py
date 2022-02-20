import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        t = []
        i = 0
        res = sys.maxsize
        s = []
        s1 = []
        for j in range(0, len(nums)):
            while s and s[-1] < nums[j]:
                s.pop()
            s.append(nums[j])
            while s and s[-1] > nums[j]:
                s.pop()
            s1.append(nums[j])
            t.append(nums[j])
            if j-i+1 == k:
                res = min(res, s[0]-s1[0])
                if s[0] == nums[i]:
                    s.pop(0)
                if s1[0] == nums[i]:
                    s1.pop(0)
                i+=1
        return res