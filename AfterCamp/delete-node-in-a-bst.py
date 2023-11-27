# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.output =  []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.output.append(node.val)
            inorder(node.right)
            
        inorder(root)
        if key in self.output:
            self.output.remove(key)
        else:
            return root
        
        def topdown(left, right):
            
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            r = TreeNode(self.output[mid])
            r.left = topdown(left, mid - 1)
            r.right = topdown(mid + 1, right)
            return r
        binaryTree = topdown(0, len(self.output) - 1)
        return binaryTree
        
        
        