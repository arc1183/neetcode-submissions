class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        b=len(s)
        c=len(t)
        if b!=c:
            return False
        for i,j in zip(s,t):
            a[ord(i)-97]+=1
            a[ord(j)-97]-=1
        if a != [0]*26:
            return False
        return True