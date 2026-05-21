class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        q=[]
        res=[]
        for i in range(len(nums)):
            if q is None:
                q.append(i)
            else:
                print(i,q)
                while (q!=[]) and nums[i] >nums[q[-1]]:
                    q.pop(-1)
                q.append(i)
                while (q!=[]) and q[0]<i-k+1:
                    q.pop(0)
            res.append(nums[q[0]])
        return res[k-1:]
