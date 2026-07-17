# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nh=None
        curr1=list1
        curr2=list2
        temp=None
        while curr1 and curr2:
            if curr1.val>=curr2.val:
                if not nh:
                    nh=curr2
                if temp:
                    temp.next=curr2
                temp=curr2
                curr2=curr2.next
            else:
                if not nh:
                    nh=curr1
                if temp:
                    temp.next=curr1
                temp=curr1
                curr1=curr1.next
        if curr1:
            if temp:
                temp.next=curr1
            temp=curr1
        elif curr2:
            if temp:
                temp.next=curr2
            temp=curr2
        return nh if nh else temp