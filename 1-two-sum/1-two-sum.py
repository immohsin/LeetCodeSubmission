class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            idx = d.get(target-nums[i])
            if idx is not None:
                return [idx, i]
            d[nums[i]] = i