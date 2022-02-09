# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recur(node, level, res):
            if not node:
                return
            if not res.get(level):
                res[level] = node.val
            recur(node.right, level+1, res)
            recur(node.left, level+1, res)
        d = {}
        res = []
        recur(root, 0, d)
        for _, v in d.items():
            res.append(v)
        return res
            
            