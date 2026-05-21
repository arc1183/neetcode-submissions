class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        mh=[]
        for i,j in zip(a.keys(),a.values()): 
            heapq.heappush(mh,(-j,i))
        return [heapq.heappop(mh)[-1] for i in range(k)]