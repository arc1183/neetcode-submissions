class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        if l1>l2:
            return False
        a=[0]*26
        for i in s1:
            a[ord(i)-97]+=1
            print(ord(i)-97)
        print(l2-l1)
        b=[0]*26
        for i in s2[:l1]:
            b[ord(i)-97]+=1    
        if a ==b:
            return True
        for i in range(1,l2-l1+1):
            print(a,b,i,i+l1)
            b[ord(s2[i+l1-1])-97]+=1
            b[ord(s2[i-1])-97]-=1
            if a==b:
                return True

        return False