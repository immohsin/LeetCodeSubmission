# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return get_num_nodes(root)

def get_num_nodes(node):
    if not node:
        return 0
    left = get_num_nodes(node.left)
    right = get_num_nodes(node.right)
    return left + right + 1