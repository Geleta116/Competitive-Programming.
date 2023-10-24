# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseLinkedList(self, head):
        if not head:
            return
        
        if not head.next:
            return head
        
        prev = head
        curr = head.next
        while curr and curr.next:
            later = curr.next
            curr.next = prev
            prev = curr
            curr = later
        curr.next = prev
        head.next  = None
        return curr
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        overflow = 0
        currL1 = self.reverseLinkedList(l1)
        currL2 = self.reverseLinkedList(l2)
        
        while currL1 and currL2:
            
            currSum = currL1.val + currL2.val+ overflow
            
            if currSum < 10:
                curr.next = ListNode(currSum)
                overflow = 0
                
            else:
                curr.next =  ListNode(currSum % 10)
               
                overflow = currSum // 10
                
            curr = curr.next
            currL1 = currL1.next
            currL2 = currL2.next
        
        while currL1:
            currSum = currL1.val + overflow
            if currSum < 10:
                curr.next = ListNode(currSum) 
                overflow = 0
            else:
                curr.next =  ListNode(currSum % 10)
                
                overflow = currSum // 10
            
            curr = curr.next
            currL1 = currL1.next
            
        while currL2:
            currSum = currL2.val + overflow
      
            if currSum < 10:
                curr.next = ListNode(currSum)  
                overflow = 0
            else:
                curr.next =  ListNode(currSum % 10)
                
                overflow = currSum // 10
           
            curr = curr.next
            currL2 = currL2.next
        
        if overflow > 0:
            curr.next = ListNode(overflow)
        return self.reverseLinkedList(dummy.next)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
                
                
            
        
