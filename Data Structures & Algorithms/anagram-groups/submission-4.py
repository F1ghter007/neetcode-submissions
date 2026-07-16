class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            temp="".join(sorted(i))
            if temp in d:
                d[temp].append(i)
            else:
                d[temp]=[i]
        return list(d.values())