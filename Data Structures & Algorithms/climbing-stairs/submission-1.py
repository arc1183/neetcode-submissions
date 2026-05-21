class Solution:
    def climbStairs(self, n: int) -> int:
        f=0
        s=1
        for i in range(n+1):
            f,s=f+s,f
        return f