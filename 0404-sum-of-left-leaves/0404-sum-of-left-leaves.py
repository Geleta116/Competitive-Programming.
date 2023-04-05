# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum  = 0
        def toLeft(root,case):
           
            if not root:
                return True
            
           

            isLeftLeaf = toLeft(root.left, True)
            isRightLeaf = toLeft(root.right, False)
            
            if case and isLeftLeaf and isRightLeaf:
                self.sum += root.val
            
        toLeft(root, False)
        return self.sum
        