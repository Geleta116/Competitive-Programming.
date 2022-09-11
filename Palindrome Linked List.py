# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis = []
        while head:
            lis.append(head.val)
            head= head.next
        i = 0
        j = -1
        check = True
        while i<(len(lis)+j):
            if lis[i]!=lis[j]:
                check = False
                break
            i+=1
            j-=1
        return check
            
