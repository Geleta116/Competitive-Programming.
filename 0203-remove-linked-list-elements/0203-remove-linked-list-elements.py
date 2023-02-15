# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy  = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        if cur and cur.next == None:
                if cur.val == val:
                    return None
                else:
                    return head
        elif dummy.next == None:
            return None
       
        elif cur.next:
            nec = cur.next
            while cur:
                if nec:
                    temp = nec.next
                    if cur.val == val:
                        prev.next = nec
                        cur = nec
                        nec = temp
                    else:
                        prev = prev.next
                        cur = cur.next
                        nec = nec.next
                else:
                     if cur.val == val:
                            prev.next = None
                            cur = None
                     else:
                            cur = cur.next
            return dummy.next
        
        
            
    
        