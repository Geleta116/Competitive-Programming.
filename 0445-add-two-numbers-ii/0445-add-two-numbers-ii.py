# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2, curr1, curr2, head, carry = [], [], l1, l2, ListNode(), 0
        out = []
        while curr1 is not None:
            stack1.append(curr1.val)
            curr1 = curr1.next
        while curr2 is not None:
            stack2.append(curr2.val)
            curr2 = curr2.next
        l1, l2 = len(stack1), len(stack2)
        for _ in range(max(l1, l2)):
            a = 0 if l1 <= 0 else stack1.pop()
            b = 0 if l2 <= 0 else stack2.pop()
            l1 -= 1
            l2 -= 1
            sum = a+b+carry
            carry = sum//10
            out.append(sum%10)
        if carry!=0:
            out.append(carry)
        out.reverse()
        j = 0
        curr = head = ListNode(0)
        while j<len(out):
            head.next = ListNode(out[j])
            head = head.next
            j+=1
        
        return curr.next
            
        
             
            
                
       
            