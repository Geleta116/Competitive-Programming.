# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(root):
            if not root:
                return 0
            left = 1 + helper(root.left)
            right = 1 + helper(root.right)
            
            depth = max(left,right)
            return depth
        
        return helper(root)