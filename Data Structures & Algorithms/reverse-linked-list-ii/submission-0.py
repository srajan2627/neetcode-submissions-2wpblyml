# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        leftprev = dummy
        curr = head
        for _ in range(left-1):
            curr = curr.next
            leftprev = leftprev.next

        prev = None

        for _ in range(right - left + 1):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
