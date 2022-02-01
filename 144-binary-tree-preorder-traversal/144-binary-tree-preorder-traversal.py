# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root == None:
            return output
        s = [root]
        while s:
            node = s.pop()
            output.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return output
            
            
