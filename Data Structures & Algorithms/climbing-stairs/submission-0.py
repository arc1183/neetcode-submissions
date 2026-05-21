class Solution:
    def climbStairs(self, n: int) -> int:
        first=1
        second=1
    
      
   
        for i in range(1,n):
            first,second=first+second,first
        return first