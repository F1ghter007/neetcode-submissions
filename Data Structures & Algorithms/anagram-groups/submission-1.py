from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        temp=[]
        for i in range(0,len(strs)):
            t={}
            for j in strs[i]:
                t[j]=t.get(j,0)+1
            d[tuple(sorted(t.items()))].append(strs[i])
        
        for j in d.values():
            temp.append(j)
        return temp  