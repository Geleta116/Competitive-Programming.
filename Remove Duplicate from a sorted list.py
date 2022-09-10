# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        new=[]
        if len(l)==0:
            return 
        else:
            new.append(l[0])
            for i in range(1,len(l)):
                if l[i]>l[i-1]:
                    new.append(l[i])
            head = ListNode(new[0])
            sol = head

            for i in range(1, len(new)):
                head.next = ListNode(new[i])
                head = head.next

            return sol
            
'''
The other solution is the below one
 class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while head and head.next:
            if head.val < head.next.val:
                head = head.next
            else:
                head.next = head.next.next
        return cur               
'''      
        
