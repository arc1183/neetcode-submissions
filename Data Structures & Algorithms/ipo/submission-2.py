from heapq import heappush,heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        a=[]
        for i in range(len(profits)):
            heappush(a,(capital[i],-profits[i]))
        mcap=w
        mp=[]
        i=0
        while (a or mp) and i<k:
            while a and mcap>=a[0][0]:
                b=heappop(a)
                heappush(mp,b[1])
           
            mcap= (mcap-heappop(mp)) if mp else mcap
            i+=1
        return mcap
            