class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        mode=max(a.values())
        for i in a:
            if a[i]== mode:
                return i