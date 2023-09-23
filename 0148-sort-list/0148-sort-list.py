# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        leftSide = head
        rightSide = temp
        
        sortedLeftSide = self.sortList(leftSide)
        sortedRightSide = self.sortList(rightSide)
        
        return self.Merge(sortedLeftSide, sortedRightSide)
    
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def Merge(self, left, right):
        tail = dummy = ListNode(0)
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
                tail =  tail.next
            else:
                tail.next = right
                right = right.next
                tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
                
        
        
        