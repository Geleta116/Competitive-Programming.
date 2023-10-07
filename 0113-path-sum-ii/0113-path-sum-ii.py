# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # urn 
        
        self.out = []
        
        def dfs(node, arr, runningSum):
            if not node:
                return
            # print(runningSum,arr, node.val)
            if not node.left and not node.right:
                if runningSum + node.val == targetSum:
                    arr.append(node.val)
                    self.out.append(arr[:])
                    arr.pop()
                return
            
            else:
                arr.append(node.val)
                if node.left:

                    dfs(node.left, arr, runningSum + node.val)
                if node.right:
                      dfs(node.right, arr, runningSum + node.val)
                arr.pop()
                return
        dfs(root, [], 0)
        return self.out
                    

        