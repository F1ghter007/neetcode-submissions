class Solution:
    def isValid(self, s: str) -> bool:
        brack={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in brack:
                if not stack:
                    return False
                else:
                    if stack[-1]!=brack.get(i,0):
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        return False