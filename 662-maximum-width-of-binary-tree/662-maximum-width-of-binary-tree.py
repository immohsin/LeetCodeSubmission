# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        res = 0
        start, end = 0, 0
        while q:
            n = len(q)
            for i in range(n):
                if i == 0:
                    start = q[0][1]
                elif i == n-1:
                    end = q[0][1]
                node, idx = q.pop(0)
                res = max(res, (end-start+1))
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
        return res
                