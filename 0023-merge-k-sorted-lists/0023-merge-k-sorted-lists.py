# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        heapq.heapify(arr)
        for item in lists:
            head = item
            while head:
                heapq.heappush(arr, head.val)
                head = head.next
        
        dummy = ListNode()
        curr = dummy
        while arr:
            current = heapq.heappop(arr)
            node = ListNode(current)
            curr.next = node
            curr = curr.next
        return dummy.next
        