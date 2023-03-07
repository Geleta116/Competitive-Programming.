# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                out.append(root.val)
                
                
            return out
        
        return helper(root)
        