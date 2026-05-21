class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if l<2:
            return l
        j=0
        length=1
        for i in range(1,l):
            if s[i] in s[j:i]:

                while s[i] in s[j:i]:
                    j+=1
            print(length,i,j,i-j)
            length=max(length,i-j+1)
        return length