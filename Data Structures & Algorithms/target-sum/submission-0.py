class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def bf(i,s):
            if i==len(nums):
                return s==target
            if (i,s) in dp:
                return dp[(i,s)]
            dp[(i,s)]=bf(i+1,s+nums[i])+bf(i+1,s-nums[i])
            return dp[(i,s)]
        return bf(0,0)