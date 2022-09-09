# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

            
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls1 = []
        ls2 = []
        cur  = list1
        while cur:
            ls1.append(cur.val)
            cur = cur.next
        cur = list2
        while cur:
            ls2.append(cur.val)
            cur = cur.next
        newl = []
        for i in ls1:
            newl.append(i)
        for j in ls2:
            newl.append(j)
        newl.sort()
        if len(newl)== 0:
            return list1
        else:
            head = ListNode(newl[0])
            cur = head
            for i in range(1,len(newl)):
                head.next = ListNode(newl[i])
                head = head.next
            return cur
        
