# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            if node.val >= low and node.val <= high:
                return leftSum + node.val + rightSum
            return leftSum + rightSum
        
        return dfs(root)
            
        