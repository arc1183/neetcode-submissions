class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(mid,piles):
            t=0
            for i in piles:
                t+=math.ceil(i/mid)
            return t 
        left=1
        right=max(piles)
        out=right
        while left<=right:
            mid=(left+right)//2
            t=time(mid,piles)
            if t<=h:
                out=mid
                right=mid-1
            else:
                left=mid+1
        return out