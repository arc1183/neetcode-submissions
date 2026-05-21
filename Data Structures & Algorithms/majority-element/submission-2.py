class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=nums[0]
        count=1
        for i in range(len(nums)):
            if count==0:
                a=nums[i]
                continue
            if a== nums[i] :
                count+=1
            else:
                count-=1
        return a

