# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        def recur(node, l):
            if node.left == None and node.right == None:
                l = [chr(ord('a') + node.val)]+l
                res.append(l.copy())
            if node.left:
                recur(node.left, [chr(ord('a') + node.val)]+l)
            if node.right:
                recur(node.right, [chr(ord('a') + node.val)]+l)
        recur(root, [])
        res.sort()
        return "".join(res[0])
            