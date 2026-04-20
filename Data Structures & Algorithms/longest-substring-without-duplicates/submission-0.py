class Solution:
    def lengthOfLongestSubstring(self, str1: str) -> int:
        L=0
        length=float('-inf')
        s=set()
        for R in range(len(str1)):
            if str1[R] not in s:
                length=max(length,R-L+1)
                s.add(str1[R])
            else:
                while str1[R] in s:
                    s.remove(str1[L])               
                    L+=1
                s.add(str1[R])
        if length==float('-inf'):
            return 0
        return length