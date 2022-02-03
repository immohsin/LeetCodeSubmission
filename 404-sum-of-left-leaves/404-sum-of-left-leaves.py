# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            if node == None:
                return
            recur(node.left)
            if node.left and node.left.left == None and node.left.right == None:
                nonlocal res
                res+=node.left.val
            recur(node.right)
        recur(root)
        return res