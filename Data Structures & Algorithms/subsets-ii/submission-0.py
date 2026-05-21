class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        self.res=[]
        def backtrack(part,i):
            if part not in self.res:
                print(part)
                self.res.append(part[:])
                
            if i>=len(nums):
                return
            part.append(nums[i])
            backtrack(part,i+1)
            part.pop(-1)
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(part,i+1)
        backtrack([],0)
        return self.res