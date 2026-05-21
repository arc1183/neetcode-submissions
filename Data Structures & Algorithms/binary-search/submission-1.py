class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(left,right,nums,target):
            if left>right:
                return -1
            mid=((left+right)//2) 
            print(nums[mid],mid,left,right)
            if(nums[mid]==target):
                return mid
            if(nums[mid]<target):
                return bsearch(mid+1,right,nums,target)
            else:
                return bsearch(left,mid-1,nums,target)
        l=len(nums)-1
        return bsearch(0,l,nums,target)