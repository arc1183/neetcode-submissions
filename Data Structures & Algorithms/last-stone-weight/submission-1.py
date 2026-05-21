class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=[-i for i in stones]
        
        heapq.heapify(s)
        while(len(s)>1):
            x=heapq.heappop(s)
            y=heapq.heappop(s)
            if x!=y:
                heapq.heappush(s,-abs(y-x))
        if not s:
            return 0
        return -s[0]