# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        x=0
        while curr:
            x+=1
            curr=curr.next
        #print(x)
        def reverse(head,prev,k):
            curr=head
            tempcount=0
            #prev=None
            while curr and tempcount <k:
                tempcount+=1
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            #if prev and curr:
                #print(prev.val,curr.val)
            return prev,curr
        curr=head
        intiialhead = None
        latestnode = None
        nextnode = None
        newhead=None
        while x>=k:
            if (curr==head):
                intiialhead=curr
                latestnode, nextnode = reverse(curr,None,k)
                newhead = latestnode
                curr=nextnode
                x=x-k     
            else:
                tempnode = intiialhead 
                intiialhead=curr
                latestnode, nextnode = reverse(curr,None,k)
                tempnode.next = latestnode
                curr = nextnode
                x=x-k
        intiialhead.next = curr
        return newhead