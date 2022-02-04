# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        get_leaf_node(root1, tree1)
        get_leaf_node(root2, tree2)
        return tree1 == tree2

def get_leaf_node(node, arr):
    if node == None:
        return
    if node.left == None and node.right == None:
        arr.append(node.val)
    get_leaf_node(node.left, arr)
    get_leaf_node(node.right, arr)
        