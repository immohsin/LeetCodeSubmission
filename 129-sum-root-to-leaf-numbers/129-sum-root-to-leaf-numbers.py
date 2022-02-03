# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def recur(node, s):
            if node == None:
                return
            if node.left == None and node.right == None:
                s+=str(node.val)
                res.append(int(s))
                return
            recur(node.left, s+str(node.val))
            recur(node.right, s+str(node.val))
        recur(root, "")
        return sum(res)