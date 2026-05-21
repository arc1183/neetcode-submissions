# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float('-inf')
      
        def p(r):
            if not r:
                return 0
            a=p(r.left)
            b=p(r.right)
            self.res=max(self.res,r.val,r.val+a,r.val+b,r.val+a+b)
            return r.val + max(a,b,0)
        print(p(root))
        return self.res
        