import heapq as h
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums.copy()
        h.heapify(self.nums)
        self.k=k
        

    def add(self, val: int) -> int:
        h.heappush(self.nums,val)
        while len(self.nums)>self.k:
            h.heappop(self.nums)
        return self.nums[0]
