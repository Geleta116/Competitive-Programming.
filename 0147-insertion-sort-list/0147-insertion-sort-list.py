# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        insert = head
        while head and head.next:
            if head.val > head.next.val:
                sorted_list = dummy
                insert = head.next
                while sorted_list.next.val < insert.val:
                    sorted_list = sorted_list.next
                head.next = insert.next
                insert.next = sorted_list.next
                sorted_list.next = insert
            else:
                head = head.next
                
        return dummy.next
    
  

        
        