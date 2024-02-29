# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0
        
        while queue:
           
            prev_node = None
            length = len(queue)
          
            
            for _ in range(length):
                curr = queue.popleft()
                
                if (level % 2 == 0 and ( curr.val % 2 == 0 or (prev_node is not None and prev_node >= curr.val))) or \
                 (level % 2 != 0 and ( curr.val % 2 != 0 or (prev_node is not None and prev_node <= curr.val))):
                    
                    return False
                
                prev_node = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        
        return True




                