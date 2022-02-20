class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        q = []
        ans = []
        for j in range(len(nums)):
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            if j-i+1 == k:
                ans.append(q[0])
                if q[0] == nums[i]:
                    q.pop(0)
                i+=1
            
        return ans