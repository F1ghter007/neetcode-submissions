# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        f=0
        while fast and fast.next:
            if slow==fast and f!=0:
                return True
            slow=slow.next
            fast=fast.next.next
            f=1
        return False

        