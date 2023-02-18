# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        later = head
        count  = 0
        while count <left-1:
            start = later
            later = later.next
            count += 1
            
        
        prev = None
        for i in range(right-left + 1):
            tmpNext = later.next
            later.next = prev
            prev = later
            later = tmpNext
            
        
        start.next.next = later
        start.next = prev
        return dummy.next