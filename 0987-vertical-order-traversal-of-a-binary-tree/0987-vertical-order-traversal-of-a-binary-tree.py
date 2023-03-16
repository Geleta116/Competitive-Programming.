# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column = defaultdict(list)
        
        def traverse(root,row,col):
            column[col].append([row,root.val])
            if root.left:
                traverse(root.left , row + 1 , col - 1)
            if root.right:
                traverse(root.right , row + 1 , col + 1)
        traverse(root,0,0)
        output = list(dict(sorted(column.items())).values())
        
        
        
        for item in output:
            item.sort()
        new = []
        for item in output:
            for each in item:
                each.pop(0)
        for item in output:
            temp = []
            for each in item:
                temp.append(each[0])
            new.append(temp)
            
                
        return new
      
    
    
    