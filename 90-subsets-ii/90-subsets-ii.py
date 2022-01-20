class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recur(arr, idx, out):
            for i in range(idx, len(nums)):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                out.append(arr[i])
                res.append(out.copy())
                recur(arr, i+1, out)
                out.pop()
        recur(nums, 0, [])
        res.append([])
        return res

#  [1], 
# [], [1],