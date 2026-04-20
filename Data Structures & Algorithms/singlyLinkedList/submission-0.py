class LinkNode:
    def __init__(self,value,nextnode=None):
        self.value=value
        self.next = nextnode
class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        curr = self.head
        temp=0
        while (curr):
            if temp == index:
                return curr.value
            curr=curr.next
            temp+=1
        return -1

        

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = LinkNode(val)
        else:
            curr=self.head
            temp = LinkNode(val)
            temp.next = self.head
            self.head = temp
  
        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = LinkNode(val)
        else:
            curr=self.head
            prev=curr
            while (curr):
                prev=curr
                curr=curr.next
            prev.next =LinkNode(val)
        

    def remove(self, index: int) -> bool:
        temp=0
        curr=self.head
        prev=curr
        if not self.head:
            return False
        while(curr):
            if temp==index:
                if curr==self.head:
                    self.head=self.head.next
                else:
                    prev.next=curr.next
                return True

            else:
                prev=curr
                curr=curr.next
                temp+=1
        return False


    def getValues(self) -> List[int]:
        temp=[]
        if not self.head:
            return temp
        curr=self.head
        while curr:
            temp.append(curr.value)
            curr=curr.next
        return temp
        
