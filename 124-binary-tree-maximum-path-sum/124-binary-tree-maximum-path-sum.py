# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -sys.maxsize
        def recur(node):
            if node == None:
                return 0 
            left = max(0, recur(node.left))
            right = max(0, recur(node.right))
            nonlocal maxi
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val
        recur(root)
        return maxi