class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp={}
        for i in strs:
            temp=[0]*26
            for j in i:
                temp[ord('a')-ord(j)]+=1
            if tuple(temp) in mapp:
                mapp[tuple(temp)].append(i)
            else:
                mapp[tuple(temp)] = [i]
            # mapp[tuple(temp)] = mapp.get(tuple(temp),set()).add(i)
        # return list(mapp.values())
        # print(mapp.values())
        return [i for i in mapp.values()]