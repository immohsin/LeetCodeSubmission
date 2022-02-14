# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def recur(node, res):
            if node == None:
                return 0
            left = getHieght(node.left, node.val)
            right = getHieght(node.right, node.val)
            res[0] = max(res[0], left + right)
            recur(node.left, res)
            recur(node.right, res)
        recur(root, res)
        return res[0]
    
def getHieght(node, val):
    if not node:
        return 0
    if node.val == val:
        left = 0 if not node.left else getHieght(node.left, node.val)
        right = 0 if not node.right else getHieght(node.right, node.val)
        return 1 + max(left, right)
    return 0
    
    
    