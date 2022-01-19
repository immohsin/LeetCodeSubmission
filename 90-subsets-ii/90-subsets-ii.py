class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def recur(arr, output):
            if len(arr) == 0:
                output = (*sorted(output),)
                res.add(output)
                return
            recur(arr[1:], output)
            output = (*output, arr[0])

            recur(arr[1:], output)

        recur(nums, tuple())
        return res