# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
LEFT = "left"
RIGHT = "right"
SAME = "same"
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        h, n, side = height(root)
        while True:
            if side == LEFT:
                h, n, side = height(n.left)
            elif side == RIGHT:
                h, n, side = height(n.right)
            else:
                return n


def height(node):
    if node == None:
        return 0, node, ""
    left = height(node.left)[0] + 1
    right = height(node.right)[0] + 1
    if left == right:
        return (right, node, SAME)
    elif right > left:
        return (right, node, RIGHT)
    else:
        return (left, node, LEFT)
                
            
            