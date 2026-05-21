class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        mlen=l+1
        i=j=0
        while i<l and j<=i:
            if sum(nums[j:i+1])>=target:
                mlen=min(mlen,i-j+1)

                j+=1
            else:
                i+=1
        return 0 if(mlen==l+1) else mlen