class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        
        n=len(matrix[0])
        m=len(matrix)
        right=(m*n)-1
        while left<=right:
            mid=(left+right)//2
            x=mid//n
            y=mid%n
            ele=matrix[x][y]
            if ele>target:
                right-=1
            elif ele<target:
                left+=1
            else:
                return True
        return False
        