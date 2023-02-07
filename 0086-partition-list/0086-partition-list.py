# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        dummy = less
        great = ListNode()
        dummy2 = great
        current = head
        while current:
            if current.val<x:
                less.next = current
                less = less.next
               
            else:
                great.next = current
                great = great.next
            current = current.next
        great.next = None
        less.next = dummy2.next
        return dummy.next
#         dummy = dummy.next
#         dummy2 = dummy2.next
#         less.next = dummy2
#         return less
        
#         def partition(self, head, x):
#     h1 = l1 = ListNode(0)
#     h2 = l2 = ListNode(0)
#     while head:
#         if head.val < x:
#             l1.next = head
#             l1 = l1.next
#         else:
#             l2.next = head
#             l2 = l2.next
#         head = head.next
#     l2.next = None
#     l1.next = h2.next
#     return h1.next
        