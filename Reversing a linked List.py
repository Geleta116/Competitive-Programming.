# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = None
        while head!=None:
            current_node = head
            head= head.next
            current_node.next =  previous_node
            previous_node = current_node
        return current_node
            
            
