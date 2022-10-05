# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
            t = []
            cc = head
            while cc:
                t.append(cc.val)
                cc = cc.next 
            tmp = head
            current_node = head
            tmp2 = head
            tmp4 = head
            tmp3 = head
            slow = 0
            while tmp2 and tmp2.next:
                tmp2 = tmp2.next.next
                tmp3 = tmp3.next
                slow+=1
           
            current_node = head
            prev = None
            while current_node!=None:
                    tmp = current_node.next
                    current_node.next = prev
                    prev = current_node
                    current_node = tmp
        
            g = 0
            val = 0
            while g<slow:
                n =  prev.val + t[g]
                val = max(val,n)
                prev = prev.next
                g+=1
            return val
                
           
        