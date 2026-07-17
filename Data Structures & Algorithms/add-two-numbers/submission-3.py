# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            curr=head
            prev=None
            while curr!=None:
                # prev=curr
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        # l1=rev(l1)
        # l2=rev(l2)
        temp1=l1
        temp2=l2
        ans=None
        que=0
        nh=None
        while temp1 or temp2:
            if not temp1:
                tempsum=temp2.val+que
                que=tempsum//10
                rem=tempsum%10
                temp2.val=rem
                if ans==None:
                    nh=temp2
                else:
                    ans.next=temp2
                ans=temp2

                temp2=temp2.next
            elif not temp2:
                tempsum=temp1.val+que
                que=tempsum//10
                rem=tempsum%10
                temp1.val=rem
                
                if ans==None:
                    nh=temp1
                else:
                    ans.next=temp1
                ans=temp1
                temp1=temp1.next

            else:
                tempsum=temp1.val+temp2.val+que
                que=tempsum//10
                rem=tempsum%10
                temp1.val=rem
                
                if ans==None:
                    nh=temp1
                else:
                    ans.next=temp1
                ans=temp1
                temp1=temp1.next
                temp2=temp2.next
            if que!=0:
                ans.next=ListNode(que)
        return nh