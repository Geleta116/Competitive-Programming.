# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.answer = 0
        temp = root
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.answer = root.val
                return
            inorder(root.right)
           
           
        inorder(temp)
        return self.answer