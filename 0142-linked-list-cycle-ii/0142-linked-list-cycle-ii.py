# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            p1 = head
            p2 = head
            new = head
            flag = False
            while (p2 and p2.next):
                p1 = p1.next
                p2 = p2.next.next
                if p1 == p2:
                    while new != p1:
                        new = new.next
                        p1 = p1.next
                    return new
            return None
            
                

        