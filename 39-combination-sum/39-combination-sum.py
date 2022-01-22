class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr, out):
            if len(arr) == 0 or sum(out) > target:
                return
            if sum(out) == target:
                res.append(out.copy())
                return
            dfs(arr[1:], out)
            out.append(arr[0])
            dfs(arr, out)
            out.pop()
        dfs(candidates, [])
        return res