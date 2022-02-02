# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = []
        q1 = []
        def preorder(node, arr):
            if node == None:
                arr.append('null')
                return
            arr.append(node.val)
            preorder(node.left, arr)
            preorder(node.right, arr)
        preorder(p, p1)
        preorder(q, q1)
        return p1 == q1