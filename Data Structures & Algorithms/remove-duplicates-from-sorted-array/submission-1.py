class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return n

        i=0
        j=0
        while(i<n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j