# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        nodes = head
        while nodes!=None:
            length+=1
            nodes = nodes.next
        i = 0
        j = 0
        while j<length-1:
            j+=2
            i+=1
        index = 0
        output = head
        while output!=None:
            if index == i:
                return output
            else:
                index+=1
                output = output.next
    
