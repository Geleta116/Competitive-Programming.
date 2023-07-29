# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.output = float("-inf")
        
      
        def dfs(node):
            if not node:
                    return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.output = max(self.output, left + node.val + right,left +node.val, right + node.val, node.val)
            return max(node.val + max(left , right), node.val)
        dfs(root)
        return self.output
        
            
                
            
            
                
            
            
            
        