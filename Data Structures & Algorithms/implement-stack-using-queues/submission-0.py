class MyStack:

    def __init__(self):
        self.a=[]            
        self.b=[]
    def push(self, x: int) -> None:
        self.b.append(x)
        while self.a !=[]:
            self.b.append(self.a.pop(0))
        self.a=self.b
        self.b=[]

    def pop(self) -> int:
        if self.a !=[]:
            return self.a.pop(0)
        return None
    def top(self) -> int:
        if self.a !=[]:
            return self.a[0]
        return None
    def empty(self) -> bool:
        if self.a==[]:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()