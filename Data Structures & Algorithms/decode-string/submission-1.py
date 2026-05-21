class Solution:
    def decodeString(self, s: str) -> str:
        
        res=[]
        for i in range(len(s)):
            if s[i]!=']':
               
                res.append(s[i])  
            else:
                a=""
                while res[-1]!='[':
                    a=res.pop(-1)+a
                res.pop(-1)
                b=""
                while res !=[] and res[-1].isdigit():
                    b=res.pop(-1)+b
                a=a*int(b)
                res.append(a)
        return "".join(res)