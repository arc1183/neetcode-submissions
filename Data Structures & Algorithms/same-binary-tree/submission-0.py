# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res=True
        def same(p,q):
            if not p and not q:
                return
            if not p or not q:
                self.res=False
                return

            if p.val != q.val:
                self.res=False
            
            same(p.left,q.left)
            same(p.right,q.right)
        same(p,q)
        return self.res