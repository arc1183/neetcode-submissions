class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for j in nums:
            if j != val:
                nums[k]=j
                k+=1
        return k