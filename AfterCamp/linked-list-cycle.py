# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # kans algorithm
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            
            if fast == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next
            
        return False
        
        
        
        #brute force approach interms of space
#         store = set()
        
#         while head:
#             if head in store:
#                 return True
#             store.add(head)
#             head = head.next
#         return False
        