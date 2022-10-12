# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        leng = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            leng+=1
        out = [0]*leng
        mono_s = []
        cur = head
        i = 0
        while cur:
            while mono_s and mono_s[-1][1]<cur.val:
                ind,t_val = mono_s.pop()
                out[ind] = cur.val
            mono_s.append([i,cur.val])
            i+=1
            cur = cur.next
        return out
            
            
        