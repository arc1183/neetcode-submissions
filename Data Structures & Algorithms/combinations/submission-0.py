class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        def b(i,sub):
            if i>n:
                if len(sub)==k:
                    self.res+=[sub[:]]
                return
            sub.append(i)
            b(i+1,sub)
            sub.pop(-1)
            b(i+1,sub)
        b(1,[])
        return self.res