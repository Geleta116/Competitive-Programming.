# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = head
        pt2 = head.next
        collect = 0
        while pt2!= None:
            if pt2.val == 0:
                pt1 = pt1.next
                pt1.val = collect
                collect = 0
            else:
                collect += pt2.val
            pt2 = pt2.next
        pt1.next = None
        return head.next
            
        