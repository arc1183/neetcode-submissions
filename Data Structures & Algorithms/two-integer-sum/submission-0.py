class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,j in enumerate(nums):
            b=target-j
            if b not in a:
                a[j]=i
            else:
                return [a[b],i]
        return []