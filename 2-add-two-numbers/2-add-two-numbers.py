# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls1 = []
        ls2 = []
        cur = l1
        while cur != None:
            ls1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur != None:
            ls2.append(cur.val)
            cur = cur.next
        ls1 = reversed(ls1)
        ls2 = reversed(ls2)
        s1 = ""
        s2 = ""
        for i in ls1:
            s1+=str(i)
        for j in ls2:
             s2+=str(j)
        sol = int(s1)+int(s2)
        sol = str(sol)
        string1  = []
        for n in range(len(sol)):
            string1.append(sol[n])
            
        anss = list(reversed(string1))
        head = ListNode(int(anss[0]))
        fin = head
            
        for i in range(1, len(anss)):
            head.next = ListNode(int(anss[i]))
            head = head.next
            
        return fin
            
        
        