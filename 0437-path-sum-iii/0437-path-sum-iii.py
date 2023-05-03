# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        
        self.output = 0
        
        def calculate(root, current):
            if not root:
                return
            calculate(root.left, current + root.val)
            calculate(root.right, current + root.val)
            if current + root.val == k:
                self.output += 1
                
        def dfs(root):
            if not root:
                return
            calculate(root, 0)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        
        return self.output
        
                
            
        