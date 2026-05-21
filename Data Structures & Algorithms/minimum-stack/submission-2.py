class MinStack:

    def __init__(self):
        self.a=[]
        self.m=[]

    def push(self, val: int) -> None:
        if self.a !=[]:
            self.m.append(min(val,self.m[-1]))
        else:
            self.m.append(val)
        self.a.append(val)
        
    def pop(self) -> None:
        if self.a != [] :
            self.a.pop(-1)
            self.m.pop(-1)  

    def top(self) -> int:
        if self.a != [] :
            return self.a[-1]
        return []

    def getMin(self) -> int:
        if self.m !=[]:
            return self.m[-1]
        return []
