# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #I am going to use merge sort for linked list
        left_p = head
        right_p = self.Mid(head)
        tmp = right_p.next
        right_p.next = None
        right_p = tmp
        
        left_p  = self.sortList(left_p)
        right_p = self.sortList(right_p)
        return self.merge(left_p,right_p)
    
    def Mid(self,head):
        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
    
    def merge(self,left_p,right_p):
        t = dummy = ListNode()
        while left_p and right_p:
            if left_p.val>right_p.val:
                t.next = right_p
                right_p = right_p.next
                t = t.next
            else:
                t.next = left_p
                left_p = left_p.next 
                t = t.next
        if left_p:
            while left_p:
                t.next = left_p
                t = t.next
                left_p = left_p.next
            
        if right_p:
            while right_p:
                t.next = right_p
                t = t.next
                right_p = right_p.next
            
       
        return dummy.next