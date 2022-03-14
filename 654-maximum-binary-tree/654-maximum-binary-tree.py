# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums):
            heap = [(-nums[i], i) for i in range(len(nums))]
            heapq.heapify(heap)
            max_val, idx = heap.pop(0)
            root = TreeNode(-max_val)
            root.left = self.constructMaximumBinaryTree(nums[:idx])
            root.right = self.constructMaximumBinaryTree(nums[idx+1:])
            return root
        else:
            return None