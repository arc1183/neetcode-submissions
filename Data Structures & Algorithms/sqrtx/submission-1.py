class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        while left<=right:
            mid=(left+right)//2
            a=mid*mid
            print(mid,a)
            if a>x:
                right=mid-1
            elif a<x:
                left=mid+1
            else:
                return mid
        return left-1