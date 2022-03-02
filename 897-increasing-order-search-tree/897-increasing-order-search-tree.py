# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        dfs(root, res)
        node = TreeNode(res.pop(0))
        t = node
        while res:
            t.right = TreeNode(res.pop(0))
            t = t.right
        return node
        
            

def dfs(node, res):
    if not node:
        return
    dfs(node.left, res)
    res.append(node.val)
    dfs(node.right, res)
    