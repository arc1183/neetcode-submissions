class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=len(arr)
        if l<k+1:
            return arr
        d=[]
        for i in range(l):
            d.append(abs(arr[i]-x))
        j=0
        m=(sum(d[:k]))
        res=arr[:k]
        for i in range(1,l-k+1):
            if(m>sum(d[i:k+i])):
                m=sum(d[i:k+i])
                res=arr[i:k+i] 
            elif sum(d[i:k+i]):
                break   

        return res

