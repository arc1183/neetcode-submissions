class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            a=[0]*26
            for j in i:
                a[ord(j)-97]+=1
            a=tuple(a)
            if a not in res:
                res[a]=[i]
            else:
                res[a].append(i)
        return list(res.values())