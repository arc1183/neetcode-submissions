class Solution:
    def countSubstrings(self, s: str) -> int:
        l=len(s)
        res=0
        dp=[[False] * l for _ in range(l)]
       
        for i in range(l):
            for j in range(i,-1,-1):
                if s[j]==s[i] and  ((i-j)<=2 or dp[i-1][j+1]):
                    dp[i][j]=True
                    res+=1
        
        return res

        