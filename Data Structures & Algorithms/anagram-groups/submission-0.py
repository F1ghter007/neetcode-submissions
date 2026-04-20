from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        count=[0]*26
        for i in range(0,len(strs)):
            count=[0]*26
            for j in (strs[i]):
                count[ord(j)-ord("a")]+=1
            res[tuple(count)].append(strs[i])
        print(res.values())
        return list(res.values())
        
