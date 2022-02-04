# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return list(get_leaf_node(root1)) == list(get_leaf_node(root2))

def get_leaf_node(node):
    if node == None:
        return
    if node.left == None and node.right == None:
        yield node.val
    yield from get_leaf_node(node.left)
    yield from get_leaf_node(node.right)
        