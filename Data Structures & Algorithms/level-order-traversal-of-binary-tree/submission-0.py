# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        a=[root]
        res=[]
        while a:
            l=len(a)
            b=[]
            for i in range(l):
                root=a.pop(0)
                b.append(root.val)
                if root.left:
                    a.append(root.left)
                if root.right:
                    a.append(root.right)
            res.append(b)
            
        return res