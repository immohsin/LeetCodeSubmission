# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1,path2 = [], []
        findPath(root, p, path1)
        findPath(root, q, path2)
        i,j = 0, 0
        ans = None
        while i< len(path1) and j < len(path2):
            if path1[i].val == path2[j].val:
                ans = path1[i]
            i+=1
            j+=1
        return ans

def findPath(node, valNode, res):
    if node == None:
        return False
    if node.val == valNode.val:
        res.append(node)
        return True
    res.append(node)
    left = findPath(node.left, valNode, res)
    right = findPath(node.right, valNode, res)
    if not left and not right:
        res.pop()
    return left or right
    
    
    
    
    
    