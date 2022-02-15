# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [(root, None)]
        while q:
            n = len(q)
            t = []
            for _ in range(n):
                node, parent = q.pop(0)
                if node.val in [x, y]:
                    t.append(parent)
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            if len(t) == 2 and t[0].val != t[1].val:
                return True
        return False