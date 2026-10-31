# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        # define fast and slow pointers
        fast = dummy
        slow = dummy

        # set n gap between fast and slow
        for _ in range(n):
            fast = fast.next
        
        # move pointers to remove position
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # remove nth node from the end of the list
        slow.next = slow.next.next

        return dummy.next