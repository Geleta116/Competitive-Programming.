# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode()
        even_dummy = ListNode()
        count = 1
        cur = head
        odd_pointer =odd_dummy
        even_pointer = even_dummy
        
        while cur:
            nxt = cur.next
            if count%2 != 0 :
                odd_pointer.next = cur
                odd_pointer = odd_pointer.next
                odd_pointer.next = None
            else:
                even_pointer.next = cur
                even_pointer = even_pointer.next
                even_pointer.next = None
            cur = nxt
            count += 1
        odd_pointer.next = even_dummy.next
        return odd_dummy.next
        
        
        
        