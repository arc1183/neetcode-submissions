class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for j in coins:
            for i in range(j,amount+1):
                if i-j>-1:
                    dp[i]+=dp[i-j]
        print(dp)
        return dp[-1]