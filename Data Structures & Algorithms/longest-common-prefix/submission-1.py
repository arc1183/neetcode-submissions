class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=min(len(strs[0]),len(strs[-1]))
        res=""
        for i in range(a):
            if strs[0][i]==strs[-1][i]:
                res+=strs[0][i]
            else: 
                break
        return res