# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.traversal = []
        
        queue = deque()
        queue.append(root)
        if root == None:
            return []
        while queue:
            temp = []
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr == None:
                    break
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    
                    queue.append(curr.right)
            self.traversal.append(temp[:])
        
        
        for index in range(len(self.traversal)):
            if index % 2 != 0:
                self.traversal[index].reverse()
        return self.traversal
                
                
            
        