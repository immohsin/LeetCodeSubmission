# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import heapq

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def postorder(node, vertical, level, res):
            if not node:
                return
            postorder(node.left, vertical-1, level+1, res)
            postorder(node.right, vertical+1, level+1, res)
            heapq.heappush(res[vertical][level], node.val)
        ans = defaultdict(lambda: defaultdict(list))
        postorder(root, 0,0, ans)
        results = []
        for vertical in sorted(ans.keys()):
            temp = []
            for level in sorted(ans[vertical].keys()):
                while(ans[vertical][level]):
                    temp.append(heapq.heappop(ans[vertical][level]))
            results.append(temp)
        return results