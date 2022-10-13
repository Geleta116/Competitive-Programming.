# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        current_node = slow.next
        prev = None
        while current_node!=None:
            tmp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = tmp
        slow.next = None
        
        a = head
        b = prev
        while a:
            temp_a = a.next
            a.next = b
            a = b
            b = temp_a
            
            
            
        
        """
        Do not return anything, modify head in-place instead.
        """
        