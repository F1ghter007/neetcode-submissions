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
        curr=head
        newhead=None
        while curr:
            #newrandom=Node(curr.random.val)
            d[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            temp=d[curr]
            if not newhead:
                newhead=temp
            if curr.next:
                temp.next=d[curr.next]
            else:
                temp.next=None
            if curr.random:
                temp.random=d[curr.random]
            else:
                temp.random=None
            curr=curr.next
        return newhead