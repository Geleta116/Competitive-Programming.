# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
      
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode(0)
        store = dummy
        while cur1 and cur2:
            num = cur1.val + cur2.val + carry
            if num>=10:
                carry = 1
                newnode = ListNode(num-10)
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                carry = 0
                newnode = ListNode(num)
                cur1 = cur1.next
                cur2 = cur2.next
            store.next = newnode
            store = store.next
        while cur1:
             num = cur1.val + carry
             if num>=10:
                carry = 1
                newnode = ListNode(num-10)
                cur1 = cur1.next
             else:
                carry = 0
                newnode = ListNode(num)
                cur1 = cur1.next
             store.next = newnode
             store = store.next
        while cur2:
             num = cur2.val + carry
             if num>=10:
                carry = 1
                newnode = ListNode(num-10)
                cur2 = cur2.next
             else:
                carry = 0
                newnode = ListNode(num)
                cur2 = cur2.next
             store.next = newnode
             store = store.next
        
        if carry>0:
            newnode = ListNode(1)
            store.next = newnode
            store = store.next
            
        return dummy.next
                
                
                
            
        
                
            
            
        
    
        
        
        
            
       