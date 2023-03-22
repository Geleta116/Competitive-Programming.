# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.out = True
        def binary(root):
            if not root:
                return 0
            left = 1 + binary(root.left)
            right = 1 + binary(root.right)
            
            if abs(left - right) > 1:
                self.out = False
                return 0
            
            return max(left,right)
        binary(root)
        return self.out
                
            
        