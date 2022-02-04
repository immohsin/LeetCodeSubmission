# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        getPreOrder(root, [], res)
        return ["->".join(r) for r in res]

def getPreOrder(node, l, res):
    if node.left == None and node.right == None:
        l.append(str(node.val))
        res.append(l.copy())
    if node.left:
        getPreOrder(node.left, l+[str(node.val)], res)
    if node.right:
        getPreOrder(node.right, l+[str(node.val)], res)
    