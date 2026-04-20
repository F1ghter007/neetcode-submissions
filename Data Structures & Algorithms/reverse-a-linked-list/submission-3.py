# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = None
        if curr==None:
            return curr
        while (curr!=None):
            temp1 = curr
            curr = curr.next
            temp1.next = temp
            temp=temp1
        return temp1

        