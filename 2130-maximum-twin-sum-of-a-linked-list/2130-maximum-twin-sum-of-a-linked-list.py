# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        dummy = ListNode(0,head)
        c = dummy
        count = 0
        while fast and fast.next and fast.next:
            count +=  1
            fast = fast.next.next
            slow = slow.next
        store = slow
        while slow and slow.next:
            c.next = slow
            c = c.next
            slow = slow.next
            
        head2 = dummy.next
        prev = None
        
        
        current_node = head2
        prev = None
        while current_node!=None:
            tmp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = tmp
            
            
       
        maxi = 0
        temp1 = head
        temp2 = prev
        while temp1 and temp2:
            compare = temp1.val +temp2.val
            maxi = max(maxi, compare)
            temp1 = temp1.next
            temp2 = temp2.next
        
        return maxi
            
        
                
                
            
        
            
        
        
        