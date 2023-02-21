# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        ct = 0
        a = head
        while a:
            ct += 1
            a = a.next
        if ct == 0:
            return None
        right = head
        left = head
        temp = head
        turn = k%ct
        if turn == 0:
            return head
        while turn:
            right = right.next
            turn-=1
        while right and right.next:
            right = right.next
            left = left.next
        store = left.next
        left.next = None
        right.next = temp
        dummy.next = store
        return dummy.next
        
            
        