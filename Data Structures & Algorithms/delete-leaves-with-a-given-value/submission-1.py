# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rl(root,t):
            if not root:
                return None
            root.left=rl(root.left,t)
            root.right=rl(root.right,t)
            if not root.left and not root.right and root.val==t:
                return None
            return root
        return rl(root,target)