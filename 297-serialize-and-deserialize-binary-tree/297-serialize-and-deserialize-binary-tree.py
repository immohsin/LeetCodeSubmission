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
        def preorder(node, arr):
            if node == None:
                arr.append('None')
                return 
            arr.append(str(node.val))
            preorder(node.left, arr)
            preorder(node.right, arr)
        res = []
        preorder(root, res)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        return buildTree(l)

def buildTree(data):
    if len(data) == 0:
        return
    ele = data.pop(0)
    if ele == 'None':
        return
    node = TreeNode(ele)
    node.left = buildTree(data)
    node.right = buildTree(data)
    return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))