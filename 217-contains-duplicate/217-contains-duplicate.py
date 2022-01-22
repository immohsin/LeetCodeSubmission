from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for i in d:
            if d[i] > 1:
                return True
        return False