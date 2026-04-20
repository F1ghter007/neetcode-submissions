class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop() + stack.pop())
            elif i=="-":
                fi = stack.pop()
                se = stack.pop()
                stack.append(se-fi)
            elif i=="*":
                stack.append(stack.pop() * stack.pop())
            elif i=="/":
                fi = stack.pop()
                se = stack.pop()
                stack.append(int(se/fi))
            else:
                stack.append(int(i))
        return int(stack.pop())