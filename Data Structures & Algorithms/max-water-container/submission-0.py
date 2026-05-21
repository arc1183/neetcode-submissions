class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j=len(heights)-1
        i=0
        w=0
        while(i<j):
            area=min(heights[i],heights[j])*(j-i)
            if(w<area):
                w=area
            
            if(heights[i]>heights[j]):
                j-=1
            else:
                i+=1
            
        return w