# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(left, right):
            if left == None and right == None:
                return True
            if (left and right == None) or (right and left == None):
                return False
            if left.val != right.val:
                return False
            return recur(left.left, right.right) and recur(left.right, right.left)
        return recur(root.left, root.right)