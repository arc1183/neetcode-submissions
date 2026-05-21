class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def r1(n):
            if not n:
                return 0
            l=len(n)
            if l==1:
                return n[0]
            
            dp=[0]*l
            dp[0]=n[0]
            dp[1]=max(n[0],n[1])
            for i in range(2,l):
                dp[i]=max(dp[i-1],dp[i-2]+n[i])
            return dp[-1]
        return max(r1(nums[:-1]),r1(nums[1:]))

