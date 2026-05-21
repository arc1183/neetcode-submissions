class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def time(weights,mid,days):
            t=1
            s=0
            for i in weights:
                s+=i
                if i>mid:
                    return False
                if s>mid:
                    t+=1
                    s=i
            return t<=days
        left=0
        right=500*(5*10**4)
        l=len(weights)
        out=right
        while left<=right:
            mid=(left+right)//2
            t=time(weights,mid,days)
            if t:
                out=min(out,mid)
                right=mid-1
            else:
                left=mid+1    
        return out