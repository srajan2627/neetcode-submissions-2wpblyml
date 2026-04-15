# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        l2 = prev

        #0->1->2->3
        #4->5->6    None<-4<-5<-6

        p1 = l1
        p2 = l2

        while p2:
            t1 = p1.next
            t2 = p2.next

            p1.next = p2
            p2.next = t1

            p1 = t1
            p2 = t2




            