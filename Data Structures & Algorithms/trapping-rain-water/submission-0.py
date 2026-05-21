class Solution:
    def trap(self, height: List[int]) -> int:
        
        i=0
        j=len(height)-1
        if j<1:
            return 0
        lm=height[i]
        rm=height[j]
        w=0
        while(i<j):
            if lm<rm:
                i+=1
                lm=max(lm,height[i])
                w+=lm-height[i]
            else:
                j-=1
                rm=max(rm,height[j])
                w+=rm-height[j]
        return w