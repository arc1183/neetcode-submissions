class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l=1
        le=mountainArr.length()-1
        r=le-1
        while l<=r:
            mid=(l+r)//2
            peak=mountainArr.get(mid)
            left=mountainArr.get(mid-1)
            right=mountainArr.get(mid+1)
            if left<peak<right:
                l=mid+1
            elif left>peak>right:
                r=mid-1
            else:
                break

                
        print("loop 1")
        print(peak)
        peak=mid
        l=0
        r=peak-1
        while l<=r:
            mid=(l+r)//2
            tar=mountainArr.get(mid)
            if tar<target:
                l=mid+1
            elif tar>target:
                r=mid-1
            else:
                return mid
        print("loop 2")
       
        l=peak
        r=le
        while l<=r:
            mid=(l+r)//2
            tar=mountainArr.get(mid)
            if tar>target:
                l=mid+1
            elif tar<target:
                r=mid-1
            else:
                return mid    
        print("loop 3")
       
        return -1
        
        
