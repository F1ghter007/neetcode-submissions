# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return curr
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        
        if length-n==0:
            return head.next
        temp=0
        curr=head
        while curr and curr.next:
            temp+=1
            if temp==length-n:
                curr.next=curr.next.next
            curr=curr.next
        return head
        