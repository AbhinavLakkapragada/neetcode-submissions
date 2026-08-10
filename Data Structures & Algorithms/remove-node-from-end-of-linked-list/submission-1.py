# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        # Make l dummy and r the head, first move r n spaces from l, then move each one 1 space, till r reaches the end, then remove l.next from it.
        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next

        # Remove the node
        left.next = left.next.next

        return dummy.next
        