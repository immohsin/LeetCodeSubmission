# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        lHeight = findHeight(root.left)
        rHeight = findHeight(root.right)
        if abs(lHeight - rHeight) > 1:
            return False
        left = self.isBalanced(root.left)
        if not left:
            return False
        right = self.isBalanced(root.right)
        if not right:
            return False
        return True

def findHeight(node):
    if node == None:
        return 0
    return 1 + max(findHeight(node.left), findHeight(node.right))