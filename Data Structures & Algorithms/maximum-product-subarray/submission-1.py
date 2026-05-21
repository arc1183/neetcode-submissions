class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=min(nums)
        cmin=1
        cmax=1
        for i in nums:
            t=cmax*i
            cmax=max(i*cmax,i*cmin,i)
            cmin=min(t,i*cmin,i)
            res=max(res,cmax)
        return res