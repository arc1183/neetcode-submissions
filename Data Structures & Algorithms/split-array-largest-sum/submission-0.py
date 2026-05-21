class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def spilt(m):
            csum=0
            spilt=1
            for i in nums:
                csum+=i
                if i>m:
                    return False
                if csum>m:
                    spilt+=1
                    csum=i
            return spilt<=k
        l=0
        r=sum(nums)
        out=r
        while l<=r:
            mid=(l+r)//2
            c=spilt(mid)
            if c:
                out=mid
                r=mid-1
            else:
                l=mid+1
                
        return out