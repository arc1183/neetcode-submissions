class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        c=min(l1,l2)
        w=""
        for i in range(c):
            w+=word1[i]+word2[i]
        if l1>l2:
            w+=word1[c:]
        elif l2>l1:
            w+=word2[c:]
        return w