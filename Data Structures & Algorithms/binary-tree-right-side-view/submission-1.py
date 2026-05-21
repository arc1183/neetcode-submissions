# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        a=[root]
        res=[]
        while a:
            if a:
                res.append(a[-1].val)
            l=len(a)
            for i in range(l):
                root=a.pop(0)
                if root.left:
                    a.append(root.left)
                if root.right:
                    a.append(root.right)
        return res