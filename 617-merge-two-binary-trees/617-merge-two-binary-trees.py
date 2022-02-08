# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return mergeTree(root1, root2)

def mergeTree(node1, node2):
    if not node1 and not node2:
        return None
    if node1 and not node2:
        return node1
    if node2 and not node1:
        return node2
    val = node1.val + node2.val
    node = TreeNode(val)
    node.left = mergeTree(node1.left, node2.left)
    node.right = mergeTree(node1.right, node2.right)
    return node
