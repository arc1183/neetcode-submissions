class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        self.res=[]
        def s(i,a):
            if i>=l:
                self.res.append(a.copy())
                return
            a.append(nums[i])
            s(i+1,a)
            a.pop(-1)
            s(i+1,a)
        s(0,[])
        return self.res