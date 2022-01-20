class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recur(arr, idx, out):
            res.append(out.copy())
            for i in range(idx, len(nums)):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                out.append(arr[i])
                recur(arr, i+1, out)
                out.pop()
        recur(nums, 0, [])
        return res
