# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return findPath(root, p, q)

def findPath(node, p, q):
    if node == None:
        return None
    if node.val in [p.val, q.val]:
        return node
    left = findPath(node.left, p, q)
    right = findPath(node.right, p, q)
    if left != None and right != None:
        return node
    return left or right
    
    
    
    
    
    