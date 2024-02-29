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

        queue = deque([(root, 0)])
        level_data = defaultdict(list)

        while queue:
            node = queue.popleft()
            
            curr_node, curr_level = node  # Unpack the tuple directly
       
            if curr_level % 2 == 0:
                if curr_node.val % 2 == 0:
                    return False
            else:
                if curr_node.val % 2 != 0:
                    return False

            if level_data[curr_level]:
                if curr_level % 2 == 0:
                    if curr_node.val % 2 == 0:
                        return False

                    if level_data[curr_level][-1] >= curr_node.val:
                        return False
                    else:
                        level_data[curr_level].append(curr_node.val)
                        if curr_node.left:
                            queue.append((curr_node.left, curr_level + 1))
                        if curr_node.right:  # Append tuple directly
                            queue.append((curr_node.right, curr_level + 1))

                else:
                    if curr_node.val % 2 != 0:
                        return False

                    if level_data[curr_level][-1] <= curr_node.val:
                        return False
                    else:
                        level_data[curr_level].append(curr_node.val)
                        if curr_node.left:
                            queue.append((curr_node.left, curr_level + 1))  # Append tuple directly
                        if curr_node.right:
                            queue.append((curr_node.right, curr_level + 1))
            else:
                level_data[curr_level].append(curr_node.val)
                if curr_node.left:
                    queue.append((curr_node.left, curr_level + 1))  # Append tuple directly
                if curr_node.right:
                    queue.append((curr_node.right, curr_level + 1))

        return True




                