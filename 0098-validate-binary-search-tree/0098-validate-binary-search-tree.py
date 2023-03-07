# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        arr = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            arr.append(root)
            if root.right:
                inorder(root.right)
            return arr
        
        inorder(root)
        for item in range(1,len(arr)):
            if arr[item].val <= arr[item - 1].val:
                return False
        return True
        
        
        
#         if not root:
#             return True
#         elif  root.left and root.left.val >= root.val:
#             return False
#         elif  root.right and root.right.val <= root.val:
#             return False
        
#         else:
#             left = self.isValidBST(root.left)
#             right = self.isValidBST(root.right)
#             return left and right
            
        