# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        def preorder(node):
            if node == None:
                l.append("x")
                return
            l.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(l)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(d):
            if len(d) == 0:
                return
            ele = d.pop(0)
            if ele == 'x':
                return
            t = TreeNode(ele)
            t.left = decode(d)
            t.right = decode(d)
            return t
        return decode(data.split(','))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))