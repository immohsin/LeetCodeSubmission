
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def permute_str(nums, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] != 'X':
                    val = nums[i]
                    perm.append(val)
                    nums[i] = 'X'
                    permute_str(nums, perm) 
                    nums[i] = perm.pop()

        permute_str(nums, perm)
        return res