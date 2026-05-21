class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        res=[0,0]
        dp=[[False] * l for _ in range(l)]
       
        for i in range(l):
            for j in range(i,-1,-1):
                if s[j]==s[i] and  ((i-j)<=2 or dp[i-1][j+1]):
                    dp[i][j]=True
                    if res[1]-res[0]<=i-j:
                        res=[j,i]
                        print(s[j:i+1],i,j)
        return s[res[0]:res[1]+1]

        