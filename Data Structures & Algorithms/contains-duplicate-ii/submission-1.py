class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        if l<2 or k<1:
            return False

        j=0
        a=[]
        for i in range(l):
            if nums[i] in a:
                return True
            if i-j<k:
                a.append(nums[i])
            else:
                a.pop(0)
                a.append(nums[i])
        return False