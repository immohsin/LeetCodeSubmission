class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,j, d, h, c = 0,0, k+1, {}, False
        while j < len(nums):
            h[nums[j]] = h.get(nums[j], 0) + 1
            if h[nums[j]] > 1:
                c = True
            if (j-i+1) > d:
                h[nums[i]] = h[nums[i]] - 1
                if h[nums[i]] ==1:
                    c = False
                i+=1
            if (j-i+1) <= d and c == True:
                    return True
            j+=1
        return False