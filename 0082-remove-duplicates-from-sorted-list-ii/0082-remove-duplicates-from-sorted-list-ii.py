# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000,head)
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                store = cur
                while store and store.next and store.val == store.next.val:
                    store = store.next
                if store.next:
                    store = store.next
                    prev.next = store
                    cur = store
                else:
                    prev.next = None
                    cur = None
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next
            
        