class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            currmin=self.minstack[-1]
            self.minstack.append(min(val,currmin))
        else:
            self.minstack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
