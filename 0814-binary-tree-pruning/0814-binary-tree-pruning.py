# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                node.left = None
            if right:
                node.right = None
            if left and right and node.val == 0:
                
                return True
            else:
                return False
        out = dfs(root)
        if out:
            return None
        return root
        