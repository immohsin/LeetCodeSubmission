# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [(root, 0)]
        d = {}
        while q:
            node, level = q.pop(0)
            if not d.get(level):
                d[level] = node.val
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))
        return [v for _,v in d.items()]