# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.hasTargetSum = False
        
        def dfs(node, runningSum):
            
            if self.hasTargetSum:
                return
            
            if not node:
                return
            
            if node.left == None and node.right == None:
                
                if runningSum + node.val == targetSum:
                    self.hasTargetSum = True
                    return
                else:
                    return
                
            dfs(node.left, runningSum + node.val)
            dfs(node.right, runningSum + node.val)
            return
        
        dfs(root, 0 )
        
        if self.hasTargetSum:
            return True
        return False
        