class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=[]
        
        position, speed =zip(*sorted(zip(position, speed)))
        print(position,speed)
        l=len(position)
        for i in range(l):
            newvec=(target-position[i])/speed[i]
            
            while a!=[] and newvec>=a[-1]:
                a.pop()
            a.append(newvec)
            
                

        print(a)
        return len(a)