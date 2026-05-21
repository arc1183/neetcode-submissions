class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={"}":"{",")":"(","]":"["}
        for i in s:
            if i in d:
                if a ==[] or a[-1]!=d[i]:
                    return False
                a.pop(-1)
            else:
                a.append(i)
        if a==[]:
            return True
        return False