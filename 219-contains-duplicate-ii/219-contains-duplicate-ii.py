class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            idx = d.get(nums[i], None)
            if idx is not None and abs(idx- i) <= k:
                return True
            d[nums[i]] = i
        return False
                