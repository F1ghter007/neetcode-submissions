"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={}
        if head == None:
            return 
        curr=head
        nhead,temp=None,None
        prev=None
        while curr:
            temp=Node(curr.val)
            d[curr] = temp
            if prev!=None:
                prev.next=temp
            if curr==head:
                nhead=temp
            curr=curr.next
            prev=temp
        prev.next=None

        curr=head
        ncurr=nhead
        while curr and ncurr:
            temprand = None
            if (curr.random):
                temprand = d[curr.random]
            ncurr.random = temprand
            curr=curr.next
            ncurr=ncurr.next
        return nhead