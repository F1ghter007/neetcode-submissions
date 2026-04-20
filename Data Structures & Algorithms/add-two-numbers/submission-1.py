# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        tempsum=0
        rem=0
        prev = None

        if curr1==None:
            return curr2
        if curr2==None:
            return curr1
        while curr1 or curr2:
            if curr1==None:
                tsum=curr2.val+rem
                rem = tsum // 10
                curr2.val = tsum % 10
                prev.next=curr2
                prev=curr2
                curr2=curr2.next
            elif curr2==None:
                tsum=curr1.val+rem
                rem = tsum // 10
                curr1.val = tsum % 10
                prev.next=curr1
                prev=curr1
                curr1=curr1.next
            else:
                tsum=curr1.val+rem + curr2.val
                rem = tsum // 10
                curr1.val = tsum % 10
                if(prev!=None):
                    prev.next=curr1
                prev=curr1
                curr1=curr1.next
                curr2=curr2.next
        if rem!=0:
            prev.next = ListNode(rem)
        return l1
        