# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.store = []
        def inorder(node):
            
            if not node:
                return
            inorder(node.left)
            self.store.append(node.val)
            inorder(node.right)
            return
        inorder(root)
     
        def rebuild(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            currNode = TreeNode(self.store[mid]) 
            currNode.left = rebuild(start, mid - 1)
            currNode.right = rebuild(mid + 1, end)
            return currNode

        
        newNode = TreeNode(self.store[len(self.store)//2])
       
        newNode.left = rebuild(0,len(self.store)//2 - 1)
        newNode.right = rebuild(len(self.store)//2+1, len(self.store)-1)
        return newNode
            
        